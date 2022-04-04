from django.db import models
from unicodedata import category

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.TextField(null=True, default='')
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
