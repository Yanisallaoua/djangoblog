from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=30)
	author = models.CharField(max_length=30)
	content = models.CharField(max_length=150)
	date = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog-home')
