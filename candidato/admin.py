from django.contrib import admin
from .models import Candidate, CandidateLinks

# Register your models here.
admin.site.register(Candidate)
admin.site.register(CandidateLinks)
