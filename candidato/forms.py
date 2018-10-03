from django.forms import ModelForm
from .models import Candidate, CandidateLinks
from django import forms


class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'nickname', 'url_name', 'political_party', 'number', 'age', 'color', 'font_color', 'bio']


class CandidateLinksForm(ModelForm):
    class Meta:
        model = CandidateLinks
        fields = ['nickname', 'twitter', 'profile', 'facebook', 'president', 'vice', 'project']

