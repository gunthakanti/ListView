from django.db import models
# Create your models here.
class Post(models.Model):
	"""docstring for Post"""
	text=models.TextField()

	# def __str__(self):
	# 	return self.text[:50]
		