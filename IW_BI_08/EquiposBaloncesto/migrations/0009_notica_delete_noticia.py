# Generated by Django 4.2.6 on 2023-11-09 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EquiposBaloncesto', '0008_noticia_imgnoticia'),
    ]

    operations = [
        migrations.CreateModel(
            name='notica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titularNoticia', models.CharField(max_length=20, unique=True)),
                ('descNoticia', models.CharField(max_length=100, unique=True)),
                ('textoImg', models.CharField(max_length=40, unique=True)),
                ('imgNoticia', models.URLField(null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noticias', to='EquiposBaloncesto.categoria')),
            ],
        ),
        migrations.DeleteModel(
            name='noticia',
        ),
    ]