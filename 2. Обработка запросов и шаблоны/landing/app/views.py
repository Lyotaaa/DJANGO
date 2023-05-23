from collections import Counter
from django.shortcuts import render

counter_show = Counter({"original": 0, "test": 0})
counter_click = Counter({"original": 0, "test": 0})


def index(request):
    req = request.GET
    if req.get("from-landing") == "original":
        counter_click["original"] += 1
    elif req.get("from-landing") == "test":
        counter_click["test"] += 1
    return render(request, "index.html")


def landing(request):
    r_G = request.GET
    if r_G["ab-test-arg"] == "original":
        counter_show["original"] += 1
        return render(request, "landing.html")
    elif r_G["ab-test-arg"] == "test":
        counter_show["test"] += 1
        return render(request, "landing_alternate.html")


def stats(request):
    if counter_show["test"]:
        test_conversion = counter_click["test"] / counter_show["test"]
    else:
        test_conversion = f"Страница тест не просматривалась"
    if counter_show["original"]:
        original_conversion = counter_click["original"] / counter_show["original"]
    else:
        original_conversion = f"Оригинальная страница не просматривалась"
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    return render(
        request,
        "stats.html",
        context={
            "test_conversion": test_conversion,
            "original_conversion": original_conversion,
        },
    )
