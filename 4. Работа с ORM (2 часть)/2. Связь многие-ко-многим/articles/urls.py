from django.urls import path
from app.views import articles_list

urlpatterns = [
    path('', articles_list, name='articles'),
]