from django.contrib import admin
from books.models import Book, BookReview, Author, BookAuthor

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title','isbn')
    list_display = ('title', 'isbn')

class BookReviewAdmin(admin.ModelAdmin):
    pass

class BookAuthorAdmin(admin.ModelAdmin):
    pass

class AuthorAdmin(admin.ModelAdmin):
    pass



admin.site.register(Book, BookAdmin)
admin.site.register(BookReview)
admin.site.register(BookAuthor)
admin.site.register(Author)
