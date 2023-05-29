from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect("catalog")


def show_catalog(request):
    sort = request.GET.get("sort")
    if sort:
        if sort == "name":
            response = Phone.objects.all().order_by("name")
        elif sort == "min_price":
            response = Phone.objects.all().order_by("price")
        elif sort == "max_price":
            response = Phone.objects.all().order_by("price").reverse()
    else:
        response = Phone.objects.all()
    context = {"phones": response}
    return render(request, "catalog.html", context)


def show_product(request, slug):
    print(slug)
    response = Phone.objects.filter(slug=slug)
    context = {"phone": response[0]}
    return render(request, "product.html", context)
