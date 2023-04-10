from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title' : forms.TextInput(attrs = {'class' :'form-control', 'placeholder' : 'Type your title'}),
            'author' : forms.TextInput(attrs = {'class' :'form-control', 'value': '', 'id' : 'user', 'type':'hidden'}),
            'category' : forms.Select(choices = choice_list, attrs = {'class' : 'form-control'}),
            'body' : forms.Textarea(attrs = {'class' :'form-control'}),
            'snippet' : forms.TextInput(attrs = {'class' :'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category', 'body', 'snippet')

        widgets = {
            'title' : forms.TextInput(attrs = {'class' :'form-control', 'placeholder' : 'Type your title'}),
            'category' : forms.Select(choices = choice_list, attrs = {'class' : 'form-control'}),
            'body' : forms.Textarea(attrs = {'class' :'form-control'}),
            'snippet' : forms.TextInput(attrs = {'class' :'form-control'}),
        }

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name' : forms.TextInput(attrs = {'class' :'form-control', 'placeholder' : 'Type your title'}),
            'body' : forms.Textarea(attrs = {'class' :'form-control'}),
        }
