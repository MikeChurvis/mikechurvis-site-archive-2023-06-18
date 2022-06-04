from django.template.loader import render_to_string
from googleapiclient.errors import Error as GoogleAPIClientError
from huey.contrib.djhuey import task

from ContactForm.models import ContactFormEntry, AdminNotificationStatus
from Emailer.gmail import get_gmail_service, create_email_data, send_email
from Emailer.models import EmailConfig


@task()
def send_contact_form_entry_as_email(contact_form_entry_id):
    # If the given contact form entry doesn't exist, the whole task is invalid.
    try:
        entry = ContactFormEntry.objects.get(id=contact_form_entry_id)
    except (KeyError, ContactFormEntry.DoesNotExist):
        raise

    try:
        config = EmailConfig.objects.get(slug=ContactFormEntry.email_config_slug)
        service = get_gmail_service()

        recipients = config.recipients.values_list('email_address', flat=True)
        carbon_copies = config.carbon_copies.values_list('email_address', flat=True)
        blind_carbon_copies = config.blind_carbon_copies.values_list('email_address', flat=True)

        subject, message = render_contact_form_entry_email(entry, recipients)

        email_data = create_email_data(
            recipients=recipients,
            carbon_copies=carbon_copies,
            blind_carbon_copies=blind_carbon_copies,
            subject=subject,
            message=message,
        )

        send_email(service, email_data)

        entry.admin_notification_status = AdminNotificationStatus.SUCCESS

    except EmailConfig.DoesNotExist:
        entry.admin_notification_status = AdminNotificationStatus.ERROR
        entry.admin_notification_detail = (
            f'EmailConfig not found. Ensure that a config entry with the slug "{ContactFormEntry.email_config_slug}" '
            'exists in the database. '
        )

    except GoogleAPIClientError as error:
        entry.admin_notification_status = AdminNotificationStatus.ERROR
        entry.admin_notification_detail = f'The Google API raised an error: {error}'

    finally:
        entry.save()


def render_contact_form_entry_email(
    entry: ContactFormEntry,
    recipients: list[str],
    subject: str = 'RE: Mike Churvis (contact form)'
) -> tuple[str, str]:
    """
    Takes a ContactFormEntry and a list of email addresses.
    Renders a subject template and message template for an email report of the contact form entry.
    Returns the rendered templates as a tuple of strings (subject, message).
    """
    render_context = {
        'name': entry.name,
        'organization': entry.organization,
        'email': entry.email,
        'message': entry.message,
        'datetime_received': entry.datetime_received,
        'reply_subject': subject,
        'reply_bcc': recipients,
    }

    subject = render_to_string('ContactForm/email_subject.txt', context=render_context)
    message = render_to_string('ContactForm/email_message.html', context=render_context)

    return subject, message
