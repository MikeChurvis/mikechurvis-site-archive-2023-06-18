from django.conf import settings
from django.db import DatabaseError

from ..models import ContactFormEntry
import pytest


# HAPPY PATHS

@pytest.mark.django_db
def test_create_with_valid_data_succeeds():
    entry = ContactFormEntry.objects.create(
        name="John Doe",
        organization="DefaultCorp Inc.",
        email="john.doe@defaultcorp.com",
        message="Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended warranty."
    )

    assert entry in ContactFormEntry.objects.all()
    assert entry.auto_forward_status == 'pending'


@pytest.mark.django_db
def test_organization_is_optional():
    entry = ContactFormEntry.objects.create(
        name="John Doe",
        email="john.doe@defaultcorp.com",
        message="Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended warranty."
    )

    assert entry in ContactFormEntry.objects.all()
    assert not entry.organization


@pytest.mark.django_db
def test_update_auto_forward_status_succeeds():
    entry = ContactFormEntry.objects.create(
        name="John Doe",
        organization="DefaultCorp Inc.",
        email="john.doe@defaultcorp.com",
        message="Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended warranty."
    )

    ContactFormEntry.objects.filter(pk=entry.pk).update(
        auto_forward_status='success'
    )

    entry.refresh_from_db()

    assert entry.auto_forward_status == 'success'


# SAD PATHS

@pytest.mark.django_db
def test_name_missing_fails():
    with pytest.raises(DatabaseError):
        ContactFormEntry.objects.create(
            organization="DefaultCorp Inc.",
            email="john.doe@defaultcorp.com",
            message="Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                    "warranty. "
        )


@pytest.mark.django_db
def test_name_too_long_fails():
    with pytest.raises(DatabaseError):
        ContactFormEntry.objects.create(
            name=f"John D{'o' * settings.CONTACTFORM_NAME_MAX_LENGTH}e",
            organization="DefaultCorp Inc.",
            email="john.doe@defaultcorp.com",
            message="Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                    "warranty. "
        )


@pytest.mark.django_db
def test_organization_too_long_fails():
    with pytest.raises(DatabaseError):
        ContactFormEntry.objects.create(
            name="John Doe",
            organization=f"DefaultC{'o' * settings.CONTACTFORM_ORGANIZATION_MAX_LENGTH}rp Inc.",
            email="john.doe@defaultcorp.com",
            message="Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                    "warranty. "
        )


@pytest.mark.django_db
def test_email_missing_fails():
    with pytest.raises(DatabaseError):
        ContactFormEntry.objects.create(
            name="John Doe",
            organization="DefaultCorp Inc.",
            message="Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                    "warranty. "
        )


@pytest.mark.django_db
def test_email_too_long_fails():
    with pytest.raises(DatabaseError):
        ContactFormEntry.objects.create(
            name="John Doe",
            organization="DefaultCorp Inc.",
            email=f"j{'o' * settings.CONTACTFORM_EMAIL_MAX_LENGTH}hn.doe@defaultcorp.com",
            message="Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                    "warranty. "
        )


# Regular expressions cannot be tested at the database level. See: form_tests.py
# @pytest.mark.django_db
# def test_email_invalid_format_fails():
#     pass


@pytest.mark.django_db
def test_message_too_short_fails():
    with pytest.raises(DatabaseError):
        ContactFormEntry.objects.create(
            name="John Doe",
            organization="DefaultCorp Inc.",
            email="john.doe@defaultcorp.com",
            message="Hi!"
        )


@pytest.mark.django_db
def test_message_missing_fails():
    with pytest.raises(DatabaseError):
        ContactFormEntry.objects.create(
            name="John Doe",
            organization="DefaultCorp Inc.",
            email="john.doe@defaultcorp.com",
        )


@pytest.mark.django_db
def test_message_too_long_fails():
    with pytest.raises(DatabaseError):
        ContactFormEntry.objects.create(
            name="John Doe",
            organization="DefaultCorp Inc.",
            email="john.doe@defaultcorp.com",
            message=f"Hi! John Doe from DefaultC{'o' * settings.CONTACTFORM_MESSAGE_MAX_LENGTH}rp here. We've been "
                    f"trying to reach you about your car's extended warranty. "
        )
