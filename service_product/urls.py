from django.urls import path
from .views import ServiceProduct

urlpatterns = [
    path('', ServiceProduct, name="service_product"),
]