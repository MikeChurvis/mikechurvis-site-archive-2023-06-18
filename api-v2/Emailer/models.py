from django.db import models
from django.utils.text import slugify


class EmailUser(models.Model):
    name = models.CharField(max_length=120)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.name} <{self.email_address}>'


class EmailConfig(models.Model):
    label = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)
    sender = models.ForeignKey(EmailUser, related_name='sender_of', on_delete=models.PROTECT)
    recipients = models.ManyToManyField(EmailUser, related_name='recipient_of')
    carbon_copies = models.ManyToManyField(EmailUser, related_name='cc_of', blank=True)
    blind_carbon_copies = models.ManyToManyField(EmailUser, related_name='bcc_of', blank=True)

    def save(self, *args, **kwargs):
        # Automatically generate a slug from the label unless a slug is provided.
        if not self.slug:
            self.slug = slugify(self.label)[:51]
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.label} Email Configuration'
