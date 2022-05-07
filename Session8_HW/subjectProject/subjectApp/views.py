from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Major, Subject
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy
# Create your views here.

class AddMajorView(CreateView):
  model = Major
  form_class = MajorModelForm
  template_name = 'add_Major_form.html'
  success_url = reverse_lazy('major_page')

class DeleteMajorView(DeleteView):
  model = Major
  #form_class = MajorModelForm
  template_name = 'delete_major_form.html'
  success_url = reverse_lazy('home')

class ListMajorView(ListView):
  model = Major
  template_name = 'major_page.html'

  def get_context_data(self, **kwargs):
    context = super(ListMajorView, self).get_context_data()
    context['subjects'] = Subject.objects.all()
    
    return context

class SubjectAddView(CreateView):
  model = Subject
  form_class = SubjectModelForm
  template_name = 'add_Subject_form.html'
  success_url = reverse_lazy('home')

class SubjectEditView(UpdateView):
  model = Subject
  form_class = SubjectModelForm
  template_name = 'edit_subject_form.html'
  success_url = reverse_lazy('home')

class SubjectDeleteView(DeleteView):
  model = Subject
  #form_class = SubjectModelForm
  template_name = 'delete_subject_form.html'
  success_url = reverse_lazy('home')

class SubjectListView(ListView):
  model = Subject
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
    context = super(SubjectListView, self).get_context_data()
    context['majors'] = Major.objects.all()
    
    return context

def major_page(request, slug):
  subjects = Subject.objects.all()
  major = Major.objects.get(slug=slug)
  
  return render(
    request,
    'major_page.html',
    {
    'subjects': subjects,
    'subject_list': Subject.objects.filter(major=major),
    'majors': Major.objects.all(),
    'major': major,
    }
  )

