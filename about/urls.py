from . import views
from django.urls import path

urlpatterns = [
    path('about/', views.about_me, name='about'),
    path('contact/', views.contact_page_view, name='contact'),
]
