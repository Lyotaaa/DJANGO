from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv


def index(request):
    return redirect(reverse("bus_stations"))


def bus_stations(request):
    with open(BUS_STATION_CSV, encoding="utf-8") as bsc:
        CONTENT = [i for i in csv.DictReader(bsc)]
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        "bus_stations": page,
        "page": page,
    }
    return render(request, "index.html", context)
