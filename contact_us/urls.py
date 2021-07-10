from django.urls import path
from .views import ContactUs

urlpatterns = [
    path('', ContactUs, name="contact_us"),
]