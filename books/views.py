from django.shortcuts import render
from django.views import View
from .models import Book

# Create your views here.
class BookView(View):
    def get(self, reqeust):
        books = Book.objects.all()
        context = {
            "books":books
        }
        return render(reqeust, "books/list.html", context)

class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        context = {
            "book":book
        }
        return render(request, "books/book_detail.html", context)
