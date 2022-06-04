import pytest
from django.conf import settings

from ..forms import ContactFormEntryForm
from ..models import ContactFormEntry


# HAPPY PATHS

@pytest.mark.django_db
def test_valid_data_is_valid_and_save_succeeds():
    entry_form = ContactFormEntryForm(data={
        "name": "John Doe",
        "organization": "DefaultCorp Inc.",
        "email": "john.doe@defaultcorp.com",
        "message": "Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                   "warranty. "
    })

    assert entry_form.is_valid()
    entry = entry_form.save()
    assert entry in ContactFormEntry.objects.all()


def test_invalid_data_is_invalid_and_save_fails():
    entry_form = ContactFormEntryForm(data={'invalidData': 'foo'})

    assert not entry_form.is_valid()
    with pytest.raises(ValueError):
        entry_form.save()


def test_organization_missing_is_valid():
    entry_form = ContactFormEntryForm(data={
        "name": "John Doe",
        "email": "john.doe@defaultcorp.com",
        "message": "Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                   "warranty. "
    })

    assert entry_form.is_valid()


# SAD PATHS

def test_name_missing_is_invalid():
    entry_form = ContactFormEntryForm(data={
        "organization": "DefaultCorp Inc.",
        "email": "john.doe@defaultcorp.com",
        "message": "Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                   "warranty. "
    })

    assert not entry_form.is_valid()


def test_name_too_long_is_invalid():
    entry_form = ContactFormEntryForm(data={
        "name": f"J{'o' * settings.CONTACTFORM_NAME_MAX_LENGTH}hn Doe",
        "organization": "DefaultCorp Inc.",
        "email": "john.doe@defaultcorp.com",
        "message": "Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                   "warranty. "
    })

    assert not entry_form.is_valid()


def test_organization_too_long_is_invalid():
    entry_form = ContactFormEntryForm(data={
        "name": "John Doe",
        "organization": f"DefaultC{'o' * settings.CONTACTFORM_ORGANIZATION_MAX_LENGTH}rp Inc.",
        "email": "john.doe@defaultcorp.com",
        "message": "Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                   "warranty. "
    })

    assert not entry_form.is_valid()


def test_email_missing_is_invalid():
    entry_form = ContactFormEntryForm(data={
        "name": "John Doe",
        "organization": f"DefaultCorp Inc.",
        "message": "Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                   "warranty. "
    })

    assert not entry_form.is_valid()


def test_email_illegal_format_is_invalid():
    entry_form = ContactFormEntryForm(data={
        "name": "John Doe",
        "organization": "DefaultCorp Inc.",
        "email": "john's invalid email",
        "message": "Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                   "warranty. "
    })

    assert not entry_form.is_valid()


def test_email_too_long_is_invalid():
    entry_form = ContactFormEntryForm(data={
        "name": "John Doe",
        "organization": "DefaultCorp Inc.",
        "email": f"j{'o' * settings.CONTACTFORM_EMAIL_MAX_LENGTH}hn.doe@defaultcorp.com",
        "message": "Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                   "warranty. "
    })

    assert not entry_form.is_valid()


def test_message_missing_is_invalid():
    entry_form = ContactFormEntryForm(data={
        "name": "John Doe",
        "organization": "DefaultCorp Inc.",
        "email": "john.doe@defaultcorp.com",
    })

    assert not entry_form.is_valid()


def test_message_too_long_is_invalid():
    entry_form = ContactFormEntryForm(data={
        "name": "John Doe",
        "organization": "DefaultCorp Inc.",
        "email": "john.doe@defaultcorp.com",
        "message": f"Hi! J{'o' * settings.CONTACTFORM_MESSAGE_MAX_LENGTH}hn Doe from DefaultCorp here. We've been "
                   "trying to reach you about your car's extended warranty. "
    })

    assert not entry_form.is_valid()


def test_message_too_short_is_invalid():
    entry_form = ContactFormEntryForm(data={
        "name": "John Doe",
        "organization": "DefaultCorp Inc.",
        "email": "john.doe@defaultcorp.com",
        "message": "Hi!"
    })

    assert not entry_form.is_valid()
