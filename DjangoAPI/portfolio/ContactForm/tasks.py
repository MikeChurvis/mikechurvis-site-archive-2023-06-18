import smtplib

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from .models import Message

@shared_task
def queue_send_message_as_email(message_id):
    """
    Takes the message with the given id and sends it as an email to the recipients
    specified in `settings.py`. This is a long-running async task that
    executes outside the HTTP request/response cycle.
    """
    message = Message.objects.get(id=message_id)
    
    try:
        send_mail(
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=settings.RECIPIENT_ADDRESS,
            subject=message.subject,
            message=message.body,
            fail_silently=False,
        )
        message.email_status = 'success'
    except smtplib.SMTPServerDisconnected:
        message.email_status = f"ERROR: Server Disconnected"
    except smtplib.SMTPSenderRefused as exc:
        message.email_status = f"ERROR: Sender Refused ({exc.sender}, {exc.smtp_error})"
    except smtplib.SMTPRecipientsRefused as exc:
        message.email_status = f"ERROR: Recipients Refused ({exc.recipients})"
    except smtplib.SMTPResponseException as exc:
        message.email_status = f"ERROR: SMTPResponseException ({exc.smtp_code}: {exc.smtp_error})"
    except smtplib.SMTPException as exc:
        message.email_status = f"ERROR: SMTPException ({str(type(exc))})"
    finally:
        message.email_status = message.email_status[:1001]
        message.save()
    
    print(f'message (id:{message.id}) email sent')
    return True