# Generated by Django 2.2.2 on 2020-01-23 19:42

from django.db import migrations, models
import fixture.models


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0005_equipo_grupo_posicion'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='posicion',
            field=models.ForeignKey(default=0, on_delete=fixture.models.Posicion, to='fixture.Posicion'),
        ),
    ]