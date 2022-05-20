from celery import shared_task
from django.conf import settings

from .models import Message
from . import gmail


@shared_task
def queue_send_message_as_email(message_id):
    """
    Takes the message with the given id and sends it as an email to the recipients
    specified in `settings.py`. This is a long-running async task that
    executes outside of the HTTP request/response cycle.
    """
    message = Message.objects.get(id=message_id)

    try:
        for recipient_address in settings.EMAIL_RECIPIENT_ADDRESS_LIST:
            message_raw = gmail.create_message(
                sender=settings.EMAIL_SENDER_ADDRESS,
                receiver=recipient_address,
                subject=message.subject,
                message_content=message.body
            )

            gmail.send_message(
                credentials_filepath=settings.GOOGLE_CLIENT_SECRET_FILEPATH,
                message=message_raw,
                token_output_path=settings.GOOGLE_CLIENT_TOKEN_FOLDER,
            )

        message.email_status = 'success'
    except gmail.HttpError as error:
        message.email_status = f"{str(type(error))} {error.status_code}: ({error.error_details})"
    finally:
        message.email_status = message.email_status[:1001]
        message.save()

    print(f'message {message.id} status: {message.email_status}')
    return True
