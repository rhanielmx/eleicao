from django.forms import ModelForm
from .models import Info
from django import forms


class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ['nickname', 'name', 'url_name']

