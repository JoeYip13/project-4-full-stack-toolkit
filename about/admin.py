from django.contrib import admin
from .models import About, Contact, ContactMessage
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('title',)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ('title', 'email', 'contact_number')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'subject', 'message', 'timestamp')
    search_fields = ['name', 'timestamp']
