from django.forms import ModelForm
from .models import Education
from django import forms


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['nickname', 'formation', 'university', 'start_date', 'end_date']

