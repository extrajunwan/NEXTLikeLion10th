from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=255)
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='post_author')

  content = models.TextField()
  
  post_image = models.ImageField(upload_to='BoardApp/images/%Y/%m/%d/', blank=True)
  created_time = models.DateTimeField(auto_now_add=True)
  updated_time = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='comment_author')
  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='author')
  
  content = models.TextField()

  def __str__(self):
    return self.content

    