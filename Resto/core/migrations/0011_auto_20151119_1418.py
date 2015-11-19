# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_seccion_id_seccion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bebida',
            new_name='Sin_Alcohol',
        ),
    ]
