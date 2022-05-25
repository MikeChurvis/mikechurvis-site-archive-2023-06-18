import json
from http import HTTPStatus
import pytest
from django.urls import reverse_lazy as reverse

from ContactForm.models import ContactFormEntry


@pytest.mark.django_db
def test_post_request_with_valid_data_responds_with_ok_status(client):
    client_form_data = {
        "name": "John Doe",
        "organization": "DefaultCorp Inc.",
        "email": "john.doe@defaultcorp.com",
        "message": "Hi! John Doe from DefaultCorp here. We've been trying to reach you about your car's extended "
                   "warranty. "
    }

    response = client.post(reverse('contact:post-form'), client_form_data)
    assert response.status_code == HTTPStatus.OK
    assert ContactFormEntry.objects.get(name="John Doe").name == "John Doe"


def test_non_post_request_responds_with_method_not_allowed_status(client):
    response = client.get(reverse('contact:post-form'))
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_post_request_with_invalid_data_responds_with_unprocessable_entity_status_and_errors(client):
    client_form_data = {}
    response = client.post(reverse('contact:post-form'), client_form_data)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    errors = json.loads(response.content)
    for required_field_name in ['name', 'email', 'message']:
        assert required_field_name in errors
