# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151110_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebida',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='plato',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
