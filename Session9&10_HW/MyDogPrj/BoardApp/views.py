from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy

# Create your views here.

def list_post(request):
  posts = Post.objects.all()

  return render(request, 'list_post.html', {'posts': posts})

def detail_post(request, post_pk):
  post = Post.objects.get(pk=post_pk)
  comments = Comment.objects.filter(post=post_pk)

  if request.method == 'POST':
    comment = Comment()
    comment.post = post
    comment.content = request.POST['comment-content']
    comment.save()
  return render(request, 'detail_post.html', {'post': post, 'comments': comments})

def delete_post(request, post_pk):
  post = Post.objects.get(pk=post_pk)
  post.delete()

  return redirect('home')

def delete_comment(request, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  post = Post.objects.get(pk=comment.post.pk)

  if request.method == 'POST':
    comment.delete()
    return render(request, 'delete_comment.html', {'comment': comment})
  return redirect('detail_post', kwargs={'post_pk': post.pk})

class PostCreate(CreateView):
  model = Post
  template_name = 'create_post.html'
  fields = ['title', 'content', 'post_image']
  #success_url = reverse_lazy('home')
  def get_success_url(self):
    return reverse_lazy('detail_post', kwargs={'post_pk': self.object.pk})

class PostUpdate(UpdateView):
  model = Post
  template_name = 'update_post.html'
  fields = ['title', 'content', 'post_image']
  
  def get_success_url(self):
    return reverse_lazy('detail_post', kwargs={'post_pk': self.object.pk})
  