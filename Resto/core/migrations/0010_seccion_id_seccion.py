# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20151119_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='seccion',
            name='id_seccion',
            field=models.IntegerField(null=True),
        ),
    ]
