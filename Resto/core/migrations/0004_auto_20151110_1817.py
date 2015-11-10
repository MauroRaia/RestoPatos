# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151110_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebida',
            name='precio',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='plato',
            name='precio',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
        ),
    ]
