from django.db import models
from datetime import datetime

# Create your models here.

class ArticleCategory(models.Model):

    category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_directory = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category

"""
class ArticleSeries(models.Model):
    series = models.CharField(max_length=200)

    series_category = models.ForeignKey(ArticleCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.series
"""

class Article(models.Model):
    article_title = models.CharField(max_length=200, default=1)
    article_content = models.TextField()
    article_published = models.DateTimeField('date published')
    article_image = models.ImageField(upload_to="images", null=True)
    article_file = models.FileField(upload_to="files", null=True)
    #https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    #article_series = models.ForeignKey(ArticleSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    article_category = models.ForeignKey(ArticleCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    article_directory = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.article_title