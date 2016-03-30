from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import auth
from django.core.context_processors import csrf
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def books(request):
    return render(request, 'blog/books.html', {})

def PSmain(request):
    return render(request, 'blog/PSmain.html', {})

def Project_M(request):
    return render(request, 'blog/Project_M.html', {})

def Data_Q(request):
    return render(request, 'blog/Data_Q.html', {})

def Master_Data(request):
    return render(request, 'blog/Master_Data.html', {})

def BI_MI(request):
    return render(request, 'blog/BI_MI.html', {})

def Data_Architecture(request):
    return render(request, 'blog/Data_Architecture.html', {})

def big_data(request):
    return render(request, 'blog/big_data.html', {})

def dcmain(request):
    return render(request, 'blog/dcmain.html', {})

def general(request):
    return render(request, 'blog/general.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
