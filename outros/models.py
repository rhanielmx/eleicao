from django.db import models
from candidato import models as candidato_models


# Create your models here.
class Info(models.Model):

    nickname = models.ForeignKey(candidato_models.Candidate, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u"Nome", max_length=150)
    url_name = models.URLField(verbose_name=u"Link", max_length=200, default='https://www.google.com/')

    def __str__(self):
        return self.name