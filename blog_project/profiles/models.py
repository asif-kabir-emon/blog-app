from django.db import models
from authors.models import Author

class Profile(models.Model):
    about = models.TextField(blank=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.author.name
