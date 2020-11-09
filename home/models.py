from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=255)
	contact = models.CharField(max_length=255, null=True, blank=True)
	address = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.name

class Book(models.Model):
	name = models.CharField(max_length = 255)
	isbn = models.CharField(max_length = 255, null = True, blank = True)
	price = models.CharField(max_length = 255, null = True, blank = True)
	book_image = models.ImageField(upload_to = "uploads/book", null = True, blank = True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.name

