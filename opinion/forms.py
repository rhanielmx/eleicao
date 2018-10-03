from django.forms import ModelForm
from .models import Opinion
from django import forms


class OpinionForm(ModelForm):
    class Meta:
        model = Opinion
        fields = ['nickname', 'name', 'url_name']

