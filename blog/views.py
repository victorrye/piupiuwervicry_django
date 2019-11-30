from django.shortcuts import render
from .forms import PostForm
from django.views.generic import ListView, DetailView
from .models import Post, Profile

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

def profile(request):
    return render(request, 'blog/profile.html', {'title': 'Profile'})

def postpiu(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    return render(request, 'users/home.html', {'form': form})

