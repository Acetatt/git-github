from django.db import models

# Create your models here.
class Category(models.Model):
	category_name = models.CharField(max_length=200)
	category_description = models.TextField()

	def __str__(self):
		return self.category_name

class Owner(models.Model):
	owner_name = models.CharField(max_length=200)
	owner_location = models.TextField()

	def __str__(self):
		return self.owner_name

class Book(models.Model):
	book_name = models.CharField(max_length=200)
	book_category = models.ForeignKey(Category,on_delete=models.CASCADE, default=None)
	book_owner = models.ForeignKey(Owner,on_delete=models.CASCADE, default=None)
	book_description = models.TextField()

	T_F = [
		("Availible", "Availible"),
        ("Not_availible", "Not availible"),
			]

	book_availibility = models.CharField(
        								 max_length=20,
        								 choices=T_F,
        								 default="Availible",
    									 )

	def __str__(self):
		return self.book_name

	def availibilities(self):
		return self.T_F

class Message(models.Model):
	message_contact = models.CharField(max_length=200)
	message_content = models.TextField()

	def __str__(self):
		return self.message_content
