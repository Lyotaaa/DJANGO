from django.shortcuts import render, reverse
from django.http import HttpResponse
import os
import datetime


def home_view(request):
    template_name = "app/home.html"
    pages = {
        "Главная страница": reverse("home"),
        "Показать текущее время": "current_time/",
        "Показать содержимое рабочей директории": "workdir_view/",
    }
    context = {"pages": pages}
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    msg = f"Текущее время: {current_time}"
    return HttpResponse(msg)


def workdir_view(request):
    list_files = " | ".join(os.listdir())
    return HttpResponse(list_files)
