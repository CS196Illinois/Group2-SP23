from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy

# Create your views here.

## def home(request):
##    return render(request, 'home.html', {})
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_time']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    # fields = '__all__'
    # fields = ('title', 'body')  # Put part of any features you want

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = UpdateForm
    #fields = ('title','body')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


