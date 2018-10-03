from django.shortcuts import render, get_object_or_404
from candidato.models import Candidate
from outros.forms import Info

# Create your views here.


def home(request):
    candidate = Candidate.objects.all().filter(nickname='Geral')
    infos = Info.objects.all().filter(nickname__nickname=candidate[0].nickname).order_by('name')

    return render(request, 'home.html',context={'infos':infos})


def about(request):
    return render(request, 'sobre.html')