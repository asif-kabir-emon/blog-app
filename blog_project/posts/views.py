from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm
from .models import Post, Comment

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('my_posts')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

@login_required
def edit_post(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('my_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

@login_required
def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('my_posts')

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'my_posts.html', {'data': posts})


# Class-based view
@method_decorator(login_required, name='dispatch')
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    success_url = reverse_lazy('my_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "edit_post.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('my_posts')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('my_posts')


@method_decorator(login_required, name='dispatch')
class PostDetailsView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = "post_details.html"
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    

    