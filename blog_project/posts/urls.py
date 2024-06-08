from django.urls import path
from .views import add_post, edit_post, delete_post, my_posts

urlpatterns = [
    path("add/", add_post, name="add_post"),
    path("edit/<int:id>", edit_post, name="edit_post"),
    path("delete/<int:id>", delete_post, name="delete_post"),
    path("my_posts/", my_posts, name="my_posts"),
]