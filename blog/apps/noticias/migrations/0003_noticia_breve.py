# Generated by Django 3.2 on 2022-12-16 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='breve',
            field=models.CharField(default='SOME STRING', max_length=120),
        ),
    ]
