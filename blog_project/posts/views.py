from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Post

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

def edit_post(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')
    
    

    