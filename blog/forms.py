from django import forms
from django.forms import CharField
from django.contrib.auth.models import User
from .models import Post
from django.forms import ModelForm

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': CharField(max_length=140),
        }
