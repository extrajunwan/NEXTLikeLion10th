from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def list_post(request):
  posts = Post.objects.all()

  return render(request, 'list_post.html', {'posts': posts})

def detail_post(request, post_pk):
  post = Post.objects.get(pk=post_pk)
  post.click
  comments = Comment.objects.filter(post=post_pk)

  if request.method == 'POST':
    # comment = Comment()
    # comment.post = post
    # comment.content = request.POST['comment-content']
    # comment.save()
    content = request.POST['comment-content']
    Comment.objects.create(post=post, content=content, author=request.user)
  return render(request, 'detail_post.html', {'post': post, 'comments': comments})

def delete_post(request, post_pk):
  post = Post.objects.get(pk=post_pk)
  post.delete()

  return redirect('home')

def delete_comment(request, post_pk, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  comment.delete()

  return redirect('detail_post', post_pk)
  # post = Post.objects.get(pk=comment.post.pk)

  # if request.method == 'POST':
  #   comment.delete()
  #   return render(request, 'delete_comment.html', {'comment': comment})
  # return redirect('detail_post', kwargs={'post_pk': post.pk})

def update_comment(request, post_pk, comment_pk):
  post = Post.objects.get(pk=post_pk)
  comment = Comment.objects.filter(pk=comment_pk)

  if request.method == 'POST':
    comment.update(
      content = request.POST['comment-content']
    )
    return redirect('detail_post', post_pk)
  return render(request, 'detail_post.html', {'post': post, 'comment': comment[0]})
 

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  template_name = 'create_post.html'
  fields = ['title', 'content', 'post_image']

  #success_url = reverse_lazy('home')
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def get_success_url(self):
    return reverse_lazy('detail_post', kwargs={'post_pk': self.object.pk})

class PostUpdate(UpdateView):
  model = Post
  template_name = 'update_post.html'
  fields = ['title', 'content', 'post_image']
  
  def get_success_url(self):
    return reverse_lazy('detail_post', kwargs={'post_pk': self.object.pk})
  
  
def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    found_user = User.objects.filter(username=username)
    if len(found_user):
      error = "이미 똑같은 아이디가 존재합니다."
      return render(request, 'registration/signup.html', {'error':error})
    new_user = User.objects.create_user(username=username, password=password)
    auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('home')
  return render(request, 'registration/signup.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
      auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
      #auth.login(request, user)

      #return redirect('home')
      return redirect(request.GET.get('next', '/'))
    error = "아이디 또는 비밀번호가 틀립니다."
    return render(request, 'registration/login.html', {'error': error})
  return render(request, 'registration/login.html')

def logout(request):
  auth.logout(request)
  
  return redirect('home')


