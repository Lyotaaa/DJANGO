from django.contrib import admin
from app.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass