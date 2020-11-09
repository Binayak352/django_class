from django.contrib import admin
from home.models import Book, Author

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ("name", "isbn", "price")
	list_filter = ("price",)
	search_fields = ("name", "isbn",)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ("name", "contact", "address")