from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import admin

class BlogPage(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='blog_img/%Y/%m/%d/', null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'updated', 'created_date')
