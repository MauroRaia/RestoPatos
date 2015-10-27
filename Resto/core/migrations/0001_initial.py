# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio_actual', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('realizado', models.BooleanField(verbose_name=b'Estado que indica si el plato fue realizado y enviado o no. Cambiar por el admin a False en el caso de no haberlo realizado y haberlo cambiado como tal.', editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('cobrado', models.BooleanField(default=True)),
                ('pedidos', models.ManyToManyField(to='core.Consumo')),
            ],
        ),
        migrations.CreateModel(
            name='Platos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cartah', models.ForeignKey(to='core.Carta', null=True)),
                ('items', models.ManyToManyField(to='core.Consumo')),
            ],
        ),
        migrations.AddField(
            model_name='consumo',
            name='seccionh',
            field=models.ForeignKey(to='core.Seccion'),
        ),
        migrations.AddField(
            model_name='carta',
            name='pedidos_actuales',
            field=models.ManyToManyField(to='core.Consumo', editable=False),
        ),
        migrations.AddField(
            model_name='carta',
            name='seccion_actual',
            field=models.ForeignKey(to='core.Seccion', null=True),
        ),
    ]
