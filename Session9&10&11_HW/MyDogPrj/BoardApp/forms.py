from .models import Post, Comment
from django import forms

'''
class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'content', 'post_image')
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목을 입력하세요.'}),
      'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '내용을 입력하세요.'}),
      'post_image': forms.ImageField
    }
'''

