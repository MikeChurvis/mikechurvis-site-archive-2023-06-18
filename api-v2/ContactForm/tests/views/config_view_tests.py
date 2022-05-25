import json
from http import HTTPStatus

from django.conf import settings
from django.urls import reverse_lazy as reverse


def test_get_request_responds_with_ok_status_values_from_settings(client):
    expected_response_body = {
      "nameMaxLength": settings.CONTACTFORM_NAME_MAX_LENGTH,
      "organizationMaxLength": settings.CONTACTFORM_ORGANIZATION_MAX_LENGTH,
      "emailMaxLength": settings.CONTACTFORM_EMAIL_MAX_LENGTH,
      "emailRegex": settings.CONTACTFORM_EMAIL_REGULAR_EXPRESSION,
      "messageMinLength": settings.CONTACTFORM_MESSAGE_MIN_LENGTH,
      "messageMaxLength": settings.CONTACTFORM_MESSAGE_MAX_LENGTH,
    }
    response = client.get(reverse('contact:config'))
    assert response.status_code == HTTPStatus.OK
    assert json.loads(response.content) == expected_response_body
