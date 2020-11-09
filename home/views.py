from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from home.models import Book, Author
from home.forms import BookForm, AuthorForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required(login_url="user:login")
def home_view(request):
	books = Book.objects.all()
	context = {"books":books}
	return render(request,"index.html", context)

def add_book(request):
	form = BookForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("app:home"))
	return render(request, "form.html",{"form":form})

class AddBookView(LoginRequiredMixin,CreateView):
	login_url = "user:login"
	model = Book
	template_name = 'form.html'
	form_class = BookForm

	def get_success_url(self):
		return reverse("app:home")

def edit_book(request, book_id):
	book = get_object_or_404(Book, id=book_id)
	form = BookForm(request.POST or None, request.FILES or None, instance=book)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("app:home"))
	return render(request, "form.html",{"form":form})

def delete_book(request, book_id):
	book = get_object_or_404(Book, id=book_id)
	form = BookForm(request.POST or None, request.FILES or None, instance=book)
	if request.method == "POST":
		book.delete()
		return HttpResponseRedirect(reverse("app:home"))
	return render(request, "delete.html", {"form":form})


def home_aview(request):
	authors = Author.objects.all()
	context = {"authors":authors}
	return render(request,"author.html", context)

def add_author(request):
	form = AuthorForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("app:home"))
	return render(request, "form.html",{"form":form})

def edit_author(request, author_id):
	author = get_object_or_404(Author, id=author_id)
	form = AuthorForm(request.POST or None, request.FILES or None, instance=author)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("app:home"))
	return render(request, "form.html",{"form":form})

def delete_author(request, author_id):
	author = get_object_or_404(Author, id=author_id)
	form = AuthorForm(request.POST or None, request.FILES or None, instance=author)
	if request.method == "POST":
		author.delete()
		return HttpResponseRedirect(reverse("app:home"))
	return render(request, "delete.html", {"form":form})

