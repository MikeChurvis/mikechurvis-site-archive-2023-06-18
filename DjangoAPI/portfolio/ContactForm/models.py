from enum import Enum

from django import forms
from django.db import models

    
    
    
    


class Message(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    email_status = models.CharField(max_length=1000, default='none')
    
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
    class Meta:
        model = Message
        fields = ['name', 'company', 'email', 'content']