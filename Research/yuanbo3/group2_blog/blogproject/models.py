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
    profile_pic = models.ImageField(null = True, blank= True, upload_to="images/profile")
    instagram_url = models.CharField(max_length=255, null = True, blank= True) # instagram
    facebook_url = models.CharField(max_length=255, null = True, blank= True) # facebook
    github_url = models.CharField(max_length=255, null = True, blank= True) # github
    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    # title_tag = models.CharField(max_length=255, default= "My awesome blog")
    header_image = models.ImageField(null = True, blank= True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    post_time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length = 255, default= "uncategorized")
    snippet = models.CharField(max_length = 255)
    like = models.ManyToManyField(User, related_name='blog_posts')


    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = "comments", on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    
    def get_absolute_url(self):
        return reverse('home')

