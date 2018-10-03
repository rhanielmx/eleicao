from django.shortcuts import render, redirect, get_object_or_404
from .models import Candidate, CandidateLinks
from experience.forms import Experience
from education.forms import Education
from opinion.forms import Opinion
from outros.forms import Info


def candidates_list(request):
    candidates = Candidate.objects.all().order_by('number')
    return render(request, 'candidates.html', {'candidates': candidates})


def candidates_profile(request, url_name):
    candidate = get_object_or_404(Candidate, url_name=url_name)
    candidate_links = CandidateLinks.objects.all().filter(nickname_id=candidate.id)
    experiences = Experience.objects.all().filter(nickname__nickname=candidate.nickname).order_by('-start_date',
                                                                                                  '-end_date')
    formations = Education.objects.all().filter(nickname__nickname=candidate.nickname).order_by('-start_date',
                                                                                                '-end_date')
    opinions = Opinion.objects.all().filter(nickname__nickname=candidate.nickname).order_by('?')
    infos = Info.objects.all().filter(nickname__nickname=candidate.nickname).order_by('?')

    context = {"candidate": candidate,
               "candidate_links": candidate_links[0],
               "experiences": experiences,
               "formations": formations,
               "opinions": opinions,
               "infos": infos
               }

    return render(request, 'candidate_profile.html', context=context)


def candidates_opinion(request, url_name):
    candidate = get_object_or_404(Candidate, url_name=url_name)
    opinions = Opinion.objects.all().filter(nickname__nickname=candidate.nickname)

    return render(request, 'candidate_opinion.html', {"candidate": candidate, "opinions": opinions})