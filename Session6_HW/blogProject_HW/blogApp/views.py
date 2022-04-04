from django.shortcuts import render, redirect
from .models import Article
from unicodedata import category 

# Create your views here.
def new(request):
  if request.method == 'POST':
    print(request.POST)
    new_article = Article.objects.create(
      title = request.POST['title'],
      category = request.POST['category'],
      content = request.POST['content'],
      updated_at = request.POST['updated_at']
    )
    return redirect('list')
  return render(request, 'new.html')

def list(request):
  articles = Article.objects.all()
  counts = len(articles)
  return render(request, 'list.html', {'articles': articles, 'count': counts})

def details(request, article_id):
  article = Article.objects.get(id=article_id)
  return render(request, 'details.html', {'article': article})

def list_hobby(request):
  articles = Article.objects.filter(category = "hobby")
  counts = len(articles)
  return render(request, 'list_hobby.html', {'articles': articles, 'count': counts})

def list_food(request):
  articles = Article.objects.filter(category = "food")
  counts = len(articles)
  return render(request, 'list_food.html', {'articles': articles, 'count': counts})

def list_programming(request):
  articles = Article.objects.filter(category = "programming")
  counts = len(articles)
  return render(request, 'list_programming.html', {'articles': articles, 'count': counts})
