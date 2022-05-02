from django import forms
from .models import Major

class MajorModelForm(forms.ModelForm):
  class Meta:
    model = Major
    fields = ('name', )
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '전공을 입력하세요.'}),
    }

    