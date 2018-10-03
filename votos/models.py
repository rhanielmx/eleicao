from django.db import models


# Create your models here.
class Vote(models.Model):
    CANDIDATOS_GROUP = (
        ('NS', 'Não Sei - 0'),
        ('CG', 'Ciro Gomes - 12'),
        ('FH', 'Fernando Haddad - 13'),
        ('HM', 'Henrique Meirelles -15'),
        ('VL', 'Vera Lúcia - 16'),
        ('JB', 'Jair Bolsonaro - 17'),
        ('MS', 'Marina Silva - 18'),
        ('AD', 'Álvaro Dias - 19'),
        ('JE', 'José Eymael - 27'),
        ('JA', 'João Amoêdo - 30'),
        ('GA', 'Geraldo Alckmin - 45'),
        ('GB', 'Guilherme Boulos - 50'),
        ('CD', 'Cabo Daciolo - 51'),
        ('JG', 'João Goulart - 54'),
    )
    SEX_GROUP = (
        ('NF', 'Não Fornecer'),
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )

    age = models.IntegerField(verbose_name=u"Idade", null=True, blank=True, default=0)
    sex = models.CharField(verbose_name=u"Sexo", max_length=30, choices=SEX_GROUP, default='NF')
    before = models.CharField(verbose_name=u"Antes de Ler *", max_length=30, choices=CANDIDATOS_GROUP)
    after = models.CharField(verbose_name=u"Depois de Ler *", max_length=30, choices=CANDIDATOS_GROUP)

    def __str__(self):
        return 'Antes: ' + self.before + ' Depois: '+ self.after