from django.contrib import admin
from .models import Article, ArticleSeries, ArticleCategory
from tinymce.widgets import TinyMCE
from django.db import models

class ArticleAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["article_title", "article_published"]}),
        ("URL", {'fields': ["article_directory"]}),
        ("Series", {'fields': ["article_series"]}),
        ("Content", {"fields": ["article_content"]}),
        ("Image", {"fields": ["article_image"]}),
        ("File", {"fields": ["article_file"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }


admin.site.register(ArticleSeries)
admin.site.register(ArticleCategory)
admin.site.register(Article,ArticleAdmin)