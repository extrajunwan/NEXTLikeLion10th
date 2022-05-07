from django.urls import path
from . import views 

urlpatterns = [
    path('add/', views.SubjectAddView.as_view(), name="addSubject"),
    path('edit/<int:pk>', views.SubjectEditView.as_view(), name="editSubject"),
    path('delete/<int:pk>', views.SubjectDeleteView.as_view(), name="deleteSubject"),
]
