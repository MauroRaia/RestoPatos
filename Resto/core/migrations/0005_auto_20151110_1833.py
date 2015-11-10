# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151110_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumo',
            old_name='seccionh',
            new_name='seccion_consumo',
        ),
        migrations.RenameField(
            model_name='seccion',
            old_name='cartah',
            new_name='carta_seccion',
        ),
        migrations.AddField(
            model_name='carta',
            name='nombre',
            field=models.CharField(default=b'Carta principal', max_length=100),
        ),
        migrations.AddField(
            model_name='seccion',
            name='nombre',
            field=models.CharField(default='Carta principal', max_length=100),
            preserve_default=False,
        ),
    ]
