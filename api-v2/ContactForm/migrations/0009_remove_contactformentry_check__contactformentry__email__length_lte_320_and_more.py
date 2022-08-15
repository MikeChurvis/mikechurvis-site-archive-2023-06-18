# Generated by Django 4.0.4 on 2022-06-01 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactForm', '0008_alter_contactformentry_message'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='contactformentry',
            name='CHECK__ContactFormEntry__email__length_LTE_320',
        ),
        migrations.RenameField(
            model_name='contactformentry',
            old_name='auto_forward_status_detail',
            new_name='admin_notification_detail',
        ),
        migrations.RenameField(
            model_name='contactformentry',
            old_name='auto_forward_status',
            new_name='admin_notification_status',
        ),
        migrations.AlterField(
            model_name='contactformentry',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AddConstraint(
            model_name='contactformentry',
            constraint=models.CheckConstraint(check=models.Q(('email__length__lte', 254)), name='CHECK__ContactFormEntry__email__length_LTE_254'),
        ),
    ]