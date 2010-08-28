from django.contrib import admin
from happydjango.book.models import Book

class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)