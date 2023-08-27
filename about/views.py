from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import About, Contact, ContactMessage
from .forms import ContactForm


def about_me(request, *args, **kwargs):
    """
    Renders the About page
    """
    about = About.objects.all().first()

    return render(
        request,
        "about.html",
        {
            "about": about
        },
    )


def contact_page_view(request, *args, **kwargs):
    """
    Renders the Contact page
    """
    submitted = False
    contact = Contact.objects.first()
    contact_messages = ContactMessage.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    form = ContactForm()

    context = {
        'contact': contact,
        'contact_messages': contact_messages,
        'form': form,
    }

    return render(
        request,
        'contact_page.html',
        context,
    )
