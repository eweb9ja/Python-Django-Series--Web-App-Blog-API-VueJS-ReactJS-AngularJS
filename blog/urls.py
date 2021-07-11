from django.urls import path
from .views import Blog, BlogCreate

urlpatterns = [
    path('', Blog, name="blog"),
    path("create/", BlogCreate, name="blog_create")
]