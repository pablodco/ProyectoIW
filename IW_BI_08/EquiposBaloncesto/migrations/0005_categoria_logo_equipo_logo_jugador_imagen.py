# Generated by Django 4.2.6 on 2023-10-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EquiposBaloncesto', '0004_alter_jugador_equipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='logo',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='equipo',
            name='logo',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='jugador',
            name='imagen',
            field=models.URLField(null=True),
        ),
    ]
