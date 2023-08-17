# Generated by Django 3.2.20 on 2023-08-17 11:00

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_contact_contactmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_image',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
