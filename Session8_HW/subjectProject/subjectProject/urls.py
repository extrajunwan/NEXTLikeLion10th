"""subjectProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from subjectApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subject/', include('subjectApp.urls')),
    path('', views.SubjectListView.as_view(), name='home'),
    path('major_page', views.ListMajorView.as_view(), name='major_page'),
    path('<str:slug>/', views.major_page),
    path('addMajor/', views.AddMajorView.as_view(), name="addMajor"),
    path('deleteMajor/<int:pk>/', views.DeleteMajorView.as_view(), name="deleteMajor"),
]
