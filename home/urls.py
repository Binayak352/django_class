from django.urls import path
from home.views import home_view, add_book, edit_book, delete_book, home_aview, add_author, edit_author, delete_author

app_name = "app"
urlpatterns = [
	path("home/", home_view, name = "home"),
	path("add_book/", add_book, name = "add_book"),
	path("edit_book/<int:book_id>/", edit_book, name="edit_book"),
	path("delete_book/<int:book_id>/delete/",delete_book, name="delete_book"),
	path("home/", home_aview, name = "home"),
	path("add_author/", add_author, name = "add_author"),
	path("edit_author/<int:author_id>/", edit_author, name="edit_author"),
	path("delete_author/<int:author_id>/delete/",delete_author, name="delete_author")
]
