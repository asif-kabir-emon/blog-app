from django.urls import path
from .views import add_post, edit_post, delete_post, my_posts, AddPostView, EditPostView, DeletePostView, PostDetailsView

urlpatterns = [
    # path("add/", add_post, name="add_post"),
    # path("edit/<int:id>", edit_post, name="edit_post"),
    # path("delete/<int:id>", delete_post, name="delete_post"),
    path("add/", AddPostView.as_view(), name="add_post"),
    path("edit/<int:id>/", EditPostView.as_view(), name="edit_post"),
    path("delete/<int:id>/", DeletePostView.as_view(), name="delete_post"),
    path("my_posts/", my_posts, name="my_posts"),
    path("details/<int:id>/", PostDetailsView.as_view(), name="post_details"),
]