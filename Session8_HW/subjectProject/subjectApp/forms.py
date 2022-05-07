from django import forms
from .models import Major, Subject

Major_Choices = Major.objects.all().values_list('name')
#values_list(): 튜플 형태의 리스트 불러옴. Entry.objects.values_list('id')로 하면 'id'에 대해서 튜플형태로 값을 가져옵니다.


class MajorModelForm(forms.ModelForm):
  class Meta:
    model = Major
    fields = ('name', )
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '전공을 입력하세요.'}),
    }


class SubjectModelForm(forms.ModelForm):
  class Meta:
    model = Subject
    fields = ('subject_name', 'major', 'prof_name', 'memo', )
    widgets = {
      'major': forms.Select(choices=Major_Choices, attrs={'class': 'form-control', }),
      'subject_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '과목명을 입력하세요.'}),
      'prof_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '교수명을 입력하세요.'}),
      'memo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '메모를 입력하세요.'}),
    }
