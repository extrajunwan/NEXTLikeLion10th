from django.urls import path, include
from . import views 

urlpatterns = [
    path('addMajor/', views.AddMajorView.as_view(), name="addMajor"),
]
