from django.contrib import admin

from Emailer.models import EmailConfig, EmailUser


@admin.register(EmailConfig)
class EmailConfigAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailUser)
class EmailUserAdmin(admin.ModelAdmin):
    pass
