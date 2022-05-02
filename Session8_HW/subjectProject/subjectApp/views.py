from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Major
from .forms import MajorModelForm
from django.urls import reverse_lazy
# Create your views here.

class AddMajorView(CreateView):
  model = Major
  form_class = MajorModelForm
  template_name = 'addMajor_form.html'
  success_url = reverse_lazy('home')
