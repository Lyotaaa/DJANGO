from pprint import pprint
from django.http import HttpResponse
from django.shortcuts import render, reverse

DATA = {
    "omlet": {
        "яйца, шт": 2,
        "молоко, л": 0.1,
        "соль, ч.л.": 0.5,
    },
    "pasta": {
        "макароны, г": 0.3,
        "сыр, г": 0.05,
    },
    "buter": {
        "хлеб, ломтик": 1,
        "колбаса, ломтик": 1,
        "сыр, ломтик": 1,
        "помидор, ломтик": 1,
    },
    # можете добавить свои рецепты ;)
}


def index(request):
    pages = {
        "Главная страница": reverse("demo"),
        "Омлет": "omlet/",
        "Паста": "pasta/",
        "Бутер": "buter/",
    }
    context = {"pages": pages}
    return render(request, "demo.html", context)


def recipes(request, meal):
    servings = request.GET.get("servings")
    new_data = dict()
    if meal in DATA:
        if servings:
            for key, value in DATA[meal].items():
                new_data[key] = value * int(servings)
            context = {"recipe": new_data}
        else:
            context = {"recipe": DATA[meal]}
    else:
        reply = "Такого рецепта не знаю :("
        context = {"reply": reply}
    return render(request, "index.html", context)
