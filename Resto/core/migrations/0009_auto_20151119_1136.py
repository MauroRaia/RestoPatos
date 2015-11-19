# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151119_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='platos',
            field=models.ForeignKey(blank=True, to='core.Plato', null=True),
        ),
    ]
