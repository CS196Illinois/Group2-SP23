from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """
    What different attributes does a post have?
    """
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #refers to the user writing the post
    body = models.TextField()

    def __str__(self):
        """
        Think of this as your toString() in Java.
        This is what post attributes will "print out" on your admin page.
        """
        return self.title + ' | ' + str(self.author)


