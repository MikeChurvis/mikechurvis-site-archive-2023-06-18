# Generated by Django 4.0.4 on 2022-05-25 22:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactForm', '0007_alter_contactformentry_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformentry',
            name='message',
            field=models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator(20)]),
        ),
    ]