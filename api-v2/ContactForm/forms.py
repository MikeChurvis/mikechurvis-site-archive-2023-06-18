from django import forms
from .models import ContactFormEntry


class ContactFormEntryForm(forms.ModelForm):
    class Meta:
        model = ContactFormEntry
        fields = ['name', 'organization', 'email', 'message']