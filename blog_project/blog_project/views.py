from django.shortcuts import render
from posts.models import Post

def home(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'home.html', {'data': posts})