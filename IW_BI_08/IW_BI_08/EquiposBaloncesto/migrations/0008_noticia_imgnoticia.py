# Generated by Django 4.2.6 on 2023-11-08 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EquiposBaloncesto', '0007_noticia'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imgNoticia',
            field=models.URLField(null=True),
        ),
    ]