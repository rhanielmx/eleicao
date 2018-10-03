# Generated by Django 2.1.1 on 2018-10-02 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, default=0, null=True, verbose_name='Idade')),
                ('sex', models.CharField(blank=True, choices=[('NF', 'Não Fornecer'), ('F', 'Feminino'), ('M', 'Masculino')], default='NF', max_length=30, null=True, verbose_name='Sexo')),
                ('before', models.CharField(choices=[('NS', 'Não Sei - 0'), ('CG', 'Ciro Gomes - 12'), ('FH', 'Fernando Haddad - 13'), ('HM', 'Henrique Meirelles -15'), ('VL', 'Vera Lúcia - 16'), ('JB', 'Jair Bolsonaro - 17'), ('MS', 'Marina Silva - 18'), ('AD', 'Álvaro Dias - 19'), ('JE', 'José Eymael - 27'), ('JA', 'João Amoêdo - 30'), ('GA', 'Geraldo Alckmin - 45'), ('GB', 'Guilherme Boulos - 50'), ('CD', 'Cabo Daciolo - 51'), ('JG', 'João Goulart - 54')], max_length=30, verbose_name='Antes de Ler *')),
                ('after', models.CharField(choices=[('NS', 'Não Sei - 0'), ('CG', 'Ciro Gomes - 12'), ('FH', 'Fernando Haddad - 13'), ('HM', 'Henrique Meirelles -15'), ('VL', 'Vera Lúcia - 16'), ('JB', 'Jair Bolsonaro - 17'), ('MS', 'Marina Silva - 18'), ('AD', 'Álvaro Dias - 19'), ('JE', 'José Eymael - 27'), ('JA', 'João Amoêdo - 30'), ('GA', 'Geraldo Alckmin - 45'), ('GB', 'Guilherme Boulos - 50'), ('CD', 'Cabo Daciolo - 51'), ('JG', 'João Goulart - 54')], max_length=30, verbose_name='Depois de Ler *')),
            ],
        ),
    ]
