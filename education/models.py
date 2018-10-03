from django.db import models
from candidato import models as candidato_models


# Create your models here.
class Education(models.Model):

    nickname = models.ForeignKey(candidato_models.Candidate, on_delete=models.CASCADE)
    formation = models.CharField(verbose_name=u"Formação", max_length=100)
    university = models.CharField(verbose_name=u"Universidade", max_length=100)
    start_date = models.CharField(verbose_name=u"Entrada na Universidade", max_length=30, null=True, blank=True, default="_")
    end_date = models.CharField(verbose_name=u"Saída da Universidade", max_length=30, null=True, blank=True, default="_")

    def __str__(self):
        return self.formation