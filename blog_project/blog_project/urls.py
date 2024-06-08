from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("category/<slug:category_slug>", home, name="categories_wise_posts"),
    path("authors/", include("authors.urls")),
    path("categories/", include("categories.urls")),
    path("posts/", include("posts.urls")),
]
