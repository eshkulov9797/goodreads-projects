from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Book

# Create your views here.
# class BookView(View):
#     def get(self, reqeust):
#         books = Book.objects.all()
#         context = {
#             "books":books
#         }
#         return render(reqeust, "books/list.html", context)

#Generic ListView dan foydanalib yozilgan
class BookView(ListView):
    template_name = 'books/list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'


# class BookDetailView(View):
#     def get(self, request, id):
#         book = Book.objects.get(id=id)
#         context = {
#             "book":book
#         }
#         return render(request, "books/book_detail.html", context)

#Generic DetailView dan foydanlaib yozilgan
class BookDetailView(DetailView):
    template_name = 'books/book_detail.html'
    pk_url_kwarg = 'id'
    model = Book