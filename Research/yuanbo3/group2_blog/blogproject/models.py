from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=255)
    # title_tag = models.CharField(max_length=255, default= "My awesome blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True) # Show the date on home page
    post_time = models.DateTimeField(auto_now_add=True) # show the specific post time in article detail page

    def __str__(self):
        """
        Think of this as your toString() in Java.
        This is what post attributes will "print out" on your admin page.
        """
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))

