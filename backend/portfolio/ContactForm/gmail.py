import base64
import json
import hashlib
import os.path
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def deterministic_hash(thing):
    dump = json.dumps(
        thing,
        ensure_ascii=False,
        sort_keys=True,
        indent=None,
        separators=(',', ':')
    )
    return hashlib.md5(dump.encode('utf-8')).digest().hex()


def get_credentials(credentials_filepath, scopes, token_output_path):
    credentials: Credentials = None
    credentials_filepath = os.path.expanduser(credentials_filepath)

    scope_hash = deterministic_hash(scopes)
    token_filepath = os.path.expanduser(os.path.join(
        token_output_path,
        f'google-client-token-{scope_hash}.secret'
    ))

    if os.path.exists(token_filepath):
        credentials = Credentials.from_authorized_user_file(
            token_filepath,
            scopes
        )

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            credentials = InstalledAppFlow.from_client_secrets_file(
                credentials_filepath,
                scopes
            ).run_local_server(port=5000)

        with open(token_filepath, 'w') as token_file:
            token_file.write(credentials.to_json())

    return credentials


def send_message(credentials_filepath, message, token_output_path='.'):
    scopes = ['https://www.googleapis.com/auth/gmail.send']
    credentials = get_credentials(
        credentials_filepath,
        scopes,
        token_output_path
    )
    service = build('gmail', 'v1', credentials=credentials)
    message = (
        service.users()
            .messages()
            .send(userId='me', body=message)
            .execute()
    )
    return message


def create_message(sender, receiver, subject, message_content):
    message = MIMEText(message_content)
    message['to'] = receiver
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


if __name__ == '__main__':
    def main():
        credentials_filepath = 'path/to/google_client.secret'
        message = create_message(
            sender='sender-address@gmail.com',
            receiver='receiver-address@gmail.com',
            subject='Testing Gmail API from Python',
            message_content="If you're reading this, the test succeeded!"
        )

        try:
            send_message(credentials_filepath, message)
        except HttpError as error:
            print(f'Error: {error}')


    main()
