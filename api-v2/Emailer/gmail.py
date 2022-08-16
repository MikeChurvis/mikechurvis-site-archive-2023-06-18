import base64
import logging
import pickle
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import google.auth.exceptions
from googleapiclient.discovery import build
from googleapiclient.errors import Error as GoogleAPIError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request as GoogleAuthRequest

from django.conf import settings
from config_helper import validate_settings

logger = logging.getLogger()

validate_settings(settings, {
    "EMAILER_TOKEN_FILEPATH",
    "EMAILER_CLIENT_SECRETS_FILEPATH",
    "EMAILER_AUTH_SCOPES",
    "EMAILER_CLIENT_EMAIL_ADDRESS",
})


def get_gmail_service():
    credentials = None

    token_path = settings.EMAILER_TOKEN_FILEPATH

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token_data:
            credentials = pickle.load(token_data)

    if not credentials or not credentials.valid:
        def initiate_auth_flow():
            logger.info('Token missing or invalid. Initiating auth flow...')
            auth_flow = InstalledAppFlow.from_client_secrets_file(
                settings.EMAILER_CLIENT_SECRETS_FILEPATH,
                settings.EMAILER_AUTH_SCOPES
            )
            new_credentials = auth_flow.run_local_server(port=5000)
            logger.info('Auth flow complete. Token generated.')
            return new_credentials

        if credentials and credentials.expired and credentials.refresh_token:
            logger.info('Token expired. Refreshing...')

            try:
                credentials.refresh(GoogleAuthRequest())
            except google.auth.exceptions.RefreshError:
                credentials = initiate_auth_flow()
            else:
                logger.info('Token refreshed.')

        else:
            credentials = initiate_auth_flow()

        with open(token_path, 'wb') as token_data:
            pickle.dump(credentials, token_data)

    service = build('gmail', 'v1', credentials=credentials)

    return service


def send_email(service, email_data: MIMEMultipart):
    try:
        encoded_email_data = base64.urlsafe_b64encode(email_data.as_string().encode('utf-8')).decode('utf-8')
        email_body = {'raw': encoded_email_data}

        email_service_response = service.users().messages().send(userId='me', body=email_body).execute()
        logger.info(f'Email Sent (ID: {email_service_response["id"]})')

    except GoogleAPIError as error:
        logger.warning(f'An error occurred while sending an email: {error}')


def create_email_data(
    recipients: tuple[str],
    subject: str,
    message: str,
    *,
    carbon_copies: tuple[str] = (),
    blind_carbon_copies: tuple[str] = ()
) -> MIMEMultipart:
    """
    Creates and returns an object containing the given email data in MIME format.
    To send this object as an email, pass it to the `send_email` function,
    along with a Gmail service resource instance.
    """
    email_data = MIMEMultipart()

    # Note that 'From' *MUST* start with a capital F. If the F is not capitalized, the email will still send, but
    # Gmail will display a 'could not verify sender identity' warning to all recipients of the email.
    email_data['From'] = settings.EMAILER_CLIENT_EMAIL_ADDRESS

    email_data['to'] = ", ".join(recipients)
    email_data['cc'] = ", ".join(carbon_copies)
    email_data['bcc'] = ", ".join(blind_carbon_copies)
    email_data['subject'] = subject
    email_data.attach(MIMEText(message, 'html'))

    return email_data
