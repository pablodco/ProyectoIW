# Generated by Django 4.2.6 on 2023-11-07 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EquiposBaloncesto', '0005_categoria_logo_equipo_logo_jugador_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='nacionalidad',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='posicion',
            field=models.CharField(max_length=30),
        ),
    ]
