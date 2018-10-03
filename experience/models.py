from django.db import models
from candidato import models as candidato_models


# Create your models here.
class Experience(models.Model):

    nickname = models.ForeignKey(candidato_models.Candidate, on_delete=models.CASCADE)
    office = models.CharField(verbose_name=u"Cargo", max_length=150)
    employer = models.CharField(verbose_name=u"Empregador", max_length=100)
    start_date = models.CharField(verbose_name=u"Entrada no Cargo", max_length=10, null=True, blank=True,  default="_")
    end_date = models.CharField(verbose_name=u"Saída do Cargo", max_length=10, null=True, blank=True, default="_")

    def __str__(self):
        return self.office