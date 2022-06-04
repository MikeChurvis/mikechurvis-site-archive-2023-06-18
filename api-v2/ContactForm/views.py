from http import HTTPStatus

from django.conf import settings
from django.http import JsonResponse

from ContactForm.forms import ContactFormEntryForm
from ContactForm.tasks import send_contact_form_entry_as_email


def get_config_data(request):
    """
    Sends form configuration data to the frontend.
    This allows clientside validation to mirror serverside validation.
    """

    return JsonResponse({
        "nameMaxLength": settings.CONTACTFORM_NAME_MAX_LENGTH,
        "organizationMaxLength": settings.CONTACTFORM_ORGANIZATION_MAX_LENGTH,
        "emailMaxLength": settings.CONTACTFORM_EMAIL_MAX_LENGTH,
        "emailRegex": settings.CONTACTFORM_EMAIL_REGULAR_EXPRESSION,
        "messageMinLength": settings.CONTACTFORM_MESSAGE_MIN_LENGTH,
        "messageMaxLength": settings.CONTACTFORM_MESSAGE_MAX_LENGTH,
    })


def post_contact_form_data(request):
    """
    Validates and saves information sent from the frontend contact form.
    Also queues the saved contact form entry to be sent as an email outside the request-response cycle.
    """

    if request.method not in ['POST']:
        return JsonResponse(
            {'allowed_methods': ['POST']},
            status=HTTPStatus.METHOD_NOT_ALLOWED
        )

    entry_form = ContactFormEntryForm(request.POST)

    if entry_form.is_valid():
        entry = entry_form.save()

        send_contact_form_entry_as_email(entry.id)  # async task

        return JsonResponse({'success': True})

    return JsonResponse(entry_form.errors, status=HTTPStatus.UNPROCESSABLE_ENTITY)
