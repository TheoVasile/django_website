from django.contrib import admin
from .models import Article
from tinymce.widgets import TinyMCE
from django.db import models

class AdminArticle(admin.ModelAdmin):
    fieldsets = [
        ('title/date', {'fields':['title','published']}),
        ('content', {'fields':['content']})
    ]

    formfield_overrides = {
        models.TextField:{'widget':TinyMCE()}
    }

# Register your models here.
admin.site.register(Article, AdminArticle)