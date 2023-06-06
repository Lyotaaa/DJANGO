from django.shortcuts import render, redirect
from books.models import Book


def index(request):
    return redirect("books/")


def books_view(request):
    template = "books/books_list.html"
    context = {"books": Book.objects.all()}
    return render(request, template, context)


def show_book_date(request, date):
    template = "books/book.html"
    all_books = Book.objects.filter(pub_date__iexact=date)
    try:
        previous_date = (
            Book.objects.filter(pub_date__lt=date)
            .values("pub_date")
            .first()["pub_date"]
            .strftime("%Y-%m-%d")
        )
    except TypeError:
        previous_date = ""
    try:
        next_date = (
            Book.objects.filter(pub_date__gt=date)
            .values("pub_date")
            .first()["pub_date"]
            .strftime("%Y-%m-%d")
        )
    except TypeError:
        next_date = ""
    context = {"books": all_books, "previous": previous_date, "next": next_date}
    return render(request, template, context)
