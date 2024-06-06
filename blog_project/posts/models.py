from django.db import models
from categories.models import Category
from authors.models import Author

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
