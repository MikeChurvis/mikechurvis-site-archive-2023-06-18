from django.contrib import admin

from .models import ContactFormEntry


@admin.register(ContactFormEntry)
class ContactFormEntryAdmin(admin.ModelAdmin):
    pass
