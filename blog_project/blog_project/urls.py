from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("authors/", include("authors.urls")),
    path("categories/", include("categories.urls")),
    path("posts/", include("posts.urls")),
]
