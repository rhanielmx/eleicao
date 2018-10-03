from django.forms import ModelForm
from .models import Experience
from django import forms


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['nickname', 'office', 'employer', 'start_date', 'end_date']

