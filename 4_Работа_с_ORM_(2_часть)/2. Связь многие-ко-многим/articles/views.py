from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = "articles/news.html"
    ordering = "-published_at"
    total_list = Article.objects.all().order_by(ordering).prefetch_related("scopes")
    context = {"object_list": total_list}
    return render(request, template, context)
