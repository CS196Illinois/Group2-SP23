from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=255)
    # title_tag = models.CharField(max_length=255, default= "My awesome blog")
    header_image = models.ImageField(null = True, blank= True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True) # show the date on home page
    post_time = models.DateTimeField(auto_now_add=True) # show the specific post time in article detail page
    category = models.CharField(max_length = 255, default= "uncategorized")
    snippet = models.CharField(max_length = 255)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')

