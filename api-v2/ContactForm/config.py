from django.core.exceptions import ImproperlyConfigured


def validate_settings(settings):
    required_settings = {
        'CONTACTFORM_NAME_MAX_LENGTH',
        'CONTACTFORM_ORGANIZATION_MAX_LENGTH',
        'CONTACTFORM_EMAIL_MAX_LENGTH',
        'CONTACTFORM_EMAIL_REGULAR_EXPRESSION',
        'CONTACTFORM_MESSAGE_MIN_LENGTH',
        'CONTACTFORM_MESSAGE_MAX_LENGTH',
    }

    missing_settings = set(filter(lambda attr: not hasattr(settings, attr), required_settings))

    if missing_settings:
        raise ImproperlyConfigured(
            'The following settings are required and are missing:\n{}'.format("\n".join(missing_settings))
        )

