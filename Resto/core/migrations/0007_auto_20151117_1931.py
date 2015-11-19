# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151110_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carta',
            name='precio_actual',
        ),
        migrations.RemoveField(
            model_name='carta',
            name='seccion_actual',
        ),
        migrations.RemoveField(
            model_name='mesa',
            name='cobrado',
        ),
        migrations.AddField(
            model_name='mesa',
            name='ip',
            field=models.CharField(default=b'[]', max_length=50, null=True, editable=False),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cobrado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='precio_actual',
            field=models.IntegerField(default=0, null=True, editable=False),
        ),
        migrations.AddField(
            model_name='pedido',
            name='seccion_actual',
            field=models.ForeignKey(blank=True, to='core.Seccion', null=True),
        ),
    ]
