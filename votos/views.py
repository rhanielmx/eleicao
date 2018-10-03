from django.shortcuts import render, redirect
from .models import Vote
from .forms import VoteForm


def get_before_votes():
    votes = Vote.objects.all()
    votes_list = []

    total_votes = votes.count()

    if total_votes > 0:
        dk_votes = votes.filter(before='NS').count()
        ciro_votes = votes.filter(before='CG').count()
        haddad_votes = votes.filter(before='FH').count()
        meirelles_votes = votes.filter(before='HM').count()
        vera_votes = votes.filter(before='VL').count()
        bolsonaro_votes = votes.filter(before='JB').count()
        marina_votes = votes.filter(before='MS').count()
        dias_votes = votes.filter(before='AD').count()
        eymael_votes = votes.filter(before='JE').count()
        amoedo_votes = votes.filter(before='JA').count()
        alckmin_votes = votes.filter(before='GA').count()
        boulos_votes = votes.filter(before='GB').count()
        daciolo_votes = votes.filter(before='CD').count()
        goulart_votes = votes.filter(before='JG').count()

        dk_pct = round(100 * dk_votes / total_votes, 2)
        ciro_pct = round(100 * ciro_votes / total_votes, 2)
        haddad_pct = round(100 * haddad_votes / total_votes, 2)
        meirelles_pct = round(100 * meirelles_votes / total_votes, 2)
        vera_pct = round(100 * vera_votes / total_votes, 2)
        bolsonaro_pct = round(100 * bolsonaro_votes / total_votes, 2)
        marina_pct = round(100 * marina_votes / total_votes, 2)
        dias_pct = round(100 * dias_votes / total_votes, 2)
        eymael_pct = round(100 * eymael_votes / total_votes, 2)
        amoedo_pct = round(100 * amoedo_votes / total_votes, 2)
        alckmin_pct = round(100 * alckmin_votes / total_votes, 2)
        boulos_pct = round(100 * boulos_votes / total_votes, 2)
        daciolo_pct = round(100 * daciolo_votes / total_votes, 2)
        goulart_pct = round(100 * goulart_votes / total_votes, 2)

        votes_list = [{'Candidate':'Indecisos','Votes':dk_pct,'Number':0},{'Candidate':'Ciro Gomes','Votes':ciro_pct,'Number':12},
                      {'Candidate':'Fernando Haddad','Votes': haddad_pct,'Number':13},{'Candidate':'Henrique Meirelles','Votes':meirelles_pct,'Number':15},
                      {'Candidate':'Vera Lúcia','Votes':vera_pct,'Number':16},{'Candidate':'Jair Bolsonaro','Votes':bolsonaro_pct,'Number':17},
                      {'Candidate':'Marina Silva','Votes':marina_pct,'Number':18},{'Candidate':'Álvaro Dias','Votes':dias_pct,'Number':19},
                      {'Candidate':'José Eymael','Votes':eymael_pct,'Number':27},{'Candidate':'João Amoedo','Votes':amoedo_pct,'Number':30},
                      {'Candidate':'Geraldo Alckimn','Votes':alckmin_pct,'Number':45},{'Candidate':'Guilherme Boulos','Votes':boulos_pct,'Number':50},
                      {'Candidate':'Cabo Daciolo','Votes':daciolo_pct,'Number':51},{'Candidates':'João Goulart','Votes':goulart_pct,'Number':54}]

    return votes_list


def get_after_votes():
    votes = Vote.objects.all()
    votes_list = []

    total_votes = votes.count()

    if total_votes > 0:
        dk_votes = votes.filter(after='NS').count()
        ciro_votes = votes.filter(after='CG').count()
        haddad_votes = votes.filter(after='FH').count()
        meirelles_votes = votes.filter(after='HM').count()
        vera_votes = votes.filter(after='VL').count()
        bolsonaro_votes = votes.filter(after='JB').count()
        marina_votes = votes.filter(after='MS').count()
        dias_votes = votes.filter(after='AD').count()
        eymael_votes = votes.filter(after='JE').count()
        amoedo_votes = votes.filter(after='JA').count()
        alckmin_votes = votes.filter(after='GA').count()
        boulos_votes = votes.filter(after='GB').count()
        daciolo_votes = votes.filter(after='CD').count()
        goulart_votes = votes.filter(after='JG').count()

        dk_pct = round(100 * dk_votes / total_votes, 2)
        ciro_pct = round(100 * ciro_votes / total_votes, 2)
        haddad_pct = round(100 * haddad_votes / total_votes, 2)
        meirelles_pct = round(100 * meirelles_votes / total_votes, 2)
        vera_pct = round(100 * vera_votes / total_votes, 2)
        bolsonaro_pct = round(100 * bolsonaro_votes / total_votes, 2)
        marina_pct = round(100 * marina_votes / total_votes, 2)
        dias_pct = round(100 * dias_votes / total_votes, 2)
        eymael_pct = round(100 * eymael_votes / total_votes, 2)
        amoedo_pct = round(100 * amoedo_votes / total_votes, 2)
        alckmin_pct = round(100 * alckmin_votes / total_votes, 2)
        boulos_pct = round(100 * boulos_votes / total_votes, 2)
        daciolo_pct = round(100 * daciolo_votes / total_votes, 2)
        goulart_pct = round(100 * goulart_votes / total_votes,2)

        votes_list = [{'Candidate':'Indecisos','Votes':dk_pct,'Number':0},{'Candidate':'Ciro Gomes','Votes':ciro_pct,'Number':12},
                      {'Candidate':'Fernando Haddad','Votes': haddad_pct,'Number':13},{'Candidate':'Henrique Meirelles','Votes':meirelles_pct,'Number':15},
                      {'Candidate':'Vera Lúcia','Votes':vera_pct,'Number':16},{'Candidate':'Jair Bolsonaro','Votes':bolsonaro_pct,'Number':17},
                      {'Candidate':'Marina Silva','Votes':marina_pct,'Number':18},{'Candidate':'Álvaro Dias','Votes':dias_pct,'Number':19},
                      {'Candidate':'José Eymael','Votes':eymael_pct,'Number':27},{'Candidate':'João Amoedo','Votes':amoedo_pct,'Number':30},
                      {'Candidate':'Geraldo Alckimn','Votes':alckmin_pct,'Number':45},{'Candidate':'Guilherme Boulos','Votes':boulos_pct,'Number':50},
                      {'Candidate':'Cabo Daciolo','Votes':daciolo_pct,'Number':51},{'Candidates':'João Goulart','Votes':goulart_pct,'Number':54}]

    return votes_list


def vote_view(request):
    form = VoteForm(request.POST or None, request.FILES or None)
    total_votes = [{'id': obj.pk, 'age': obj.age, 'sex': obj.get_sex_display(), 'before': obj.get_before_display()[:-4], 'after': obj.get_after_display()[:-4]} for obj in Vote.objects.all()]

    before_votes_list = get_before_votes()
    after_votes_list = get_after_votes()

    context = {'form': form,
               'total_votes': total_votes,
               'before_votes_list': before_votes_list,
               'after_votes_list': after_votes_list
               }

    if form.is_valid():
        form.save()
        return redirect('vote_view')
    return render(request, 'vote.html', context=context)