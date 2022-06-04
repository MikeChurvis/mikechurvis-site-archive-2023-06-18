import pytest
from django.conf import settings

from ContactForm.models import ContactFormEntry, AdminNotificationStatus
from ContactForm.tasks import send_contact_form_entry_as_email
from Emailer.models import EmailConfig, EmailUser


@pytest.fixture
def fixture__contact_form_entry(db):
    return ContactFormEntry.objects.create(
        name='John Doe',
        organization='TestCo',
        email='john.doe@testco.org',
        message="Hi! This is John Doe from TestCo Incorporated. "
                "We've been trying to reach you about your car's extended warranty."
    )


@pytest.fixture
def fixture__sender(db):
    sender = EmailUser.objects.create(
        name="Portfolio Website Mailbot",
        email_address=settings.EMAILER_CLIENT_EMAIL_ADDRESS
    )
    return sender


@pytest.fixture
def fixture__email_config(db, fixture__sender):
    sender = fixture__sender
    recipients = [sender]
    config = EmailConfig.objects.create(
        label="Contact Form",
        slug=ContactFormEntry.email_config_slug,
        sender=sender,
    )
    config.recipients.set(recipients)

    return config


def test_smoketest(fixture__contact_form_entry, fixture__email_config, fixture__sender):
    # Make sure the task queue is running in debug mode.
    assert settings.HUEY.immediate

    send_contact_form_entry_as_email(fixture__contact_form_entry.id)()
    fixture__contact_form_entry.refresh_from_db()
    assert fixture__contact_form_entry.admin_notification_status == AdminNotificationStatus.SUCCESS
