from django.shortcuts import render
from posts.models import Post
from categories.models import Category

def home(request, category_slug = None):
    print(category_slug)
    posts = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        posts = Post.objects.filter(categories = category)
    categories = Category.objects.all()
    return render(request, 'home.html', {'posts': posts, 'categories': categories})