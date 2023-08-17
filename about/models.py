from django.db import models
from cloudinary.models import CloudinaryField
from phone_field import PhoneField


class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    email = models.EmailField()
    contact_number = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
