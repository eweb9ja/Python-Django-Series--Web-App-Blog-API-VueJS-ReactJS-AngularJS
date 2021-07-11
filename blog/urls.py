from django.urls import path
from .views import Blog, BlogCreate, ShowBlog

urlpatterns = [
    path('', Blog, name="blog"),
    path("create/", BlogCreate, name="blog_create"),
    path("show/<path:id>/", ShowBlog, name="blog_show")
]