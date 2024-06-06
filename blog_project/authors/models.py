from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name
