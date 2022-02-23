from enum import Enum

from django import forms
from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=120)
    company = models.CharField(max_length=180, blank=True)
    email = models.EmailField()
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    email_status = models.CharField(max_length=1000, default='')

    class Meta:
        ordering = ['sent_at']

        indexes = [
            models.Index(fields=('sent_at',))
        ]

    def __str__(self):
        return f"[{self.sent_at}] {self.name} from {self.email}: {self.content[:100]}"

    @property
    def subject(self):
        return f"[CONTACT FORM] New message from {self.name} ({self.company or 'no company given'})"

    @property
    def body(self):
        body_string = f'On {self.sent_at.date()} at {self.sent_at.time()},'
        body_string += f'\n{self.name} from {self.company}' if self.company else f'{self.name}'
        body_string += f' <{self.email}>'
        body_string += f'\nsent the following message:\n\n\n{self.content}'

        return body_string


class MessageForm(forms.ModelForm):
    # Maps a model field to its HttpRequest param counterpart. Use this
    # when the model field and request param have different names.
    field_name_mapping = {
        'content': 'messageContent',
    }

    def add_prefix(self, field_name):
        # look up field name; return original if not found.
        field_name = self.field_name_mapping.get(field_name, field_name)
        return super(MessageForm, self).add_prefix(field_name)

    class Meta:
        model = Message
        fields = ['name', 'company', 'email', 'content']
