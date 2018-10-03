from django.db import models


# Create your models here.
class Candidate(models.Model):

    name = models.CharField(verbose_name=u"Nome", max_length=100)
    nickname = models.CharField(verbose_name=u"Apelido", max_length=25)
    url_name = models.CharField(verbose_name=u"Nome na URL", max_length=25, default='candidato')
    vice = models.CharField(verbose_name=u"Nome do Vice", max_length=25, default='vice')
    political_party = models.CharField(verbose_name=u"Partido", max_length=30)
    number = models.IntegerField(verbose_name=u"Número")
    age = models.IntegerField(verbose_name=u"Idade")
    color = models.CharField(verbose_name=u"Cor do Partido", max_length=25, default='orange')
    font_color = models.CharField(verbose_name=u"Cor da fonte", max_length=25, default='orange')
    bio = models.TextField(verbose_name=u"Biografia", null=True, blank=True)

    def __str__(self):
        return self.nickname


class CandidateLinks(models.Model):

    nickname = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    twitter = models.URLField(verbose_name=u"Twitter", max_length=200, default='https://twitter.com/')
    profile = models.URLField(verbose_name=u"Perfil", max_length=200, default='http://lattes.cnpq.br/')
    facebook = models.URLField(verbose_name=u"Facebook", max_length=200, default='https://www.facebook.com/')
    president = models.URLField(verbose_name=u"Presidente", max_length=200, default='https://www.google.com/')
    vice = models.URLField(verbose_name=u"vice", max_length=200, default='https://www.google.com/')
    project = models.URLField(verbose_name=u"Projeto", max_length=200, default='https://www.google.com/')

    def __str__(self):
        return str(self.nickname)