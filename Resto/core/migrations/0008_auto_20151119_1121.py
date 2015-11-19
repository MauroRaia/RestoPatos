# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151117_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_interno', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='mesa',
            name='ip',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cobrado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='platos',
            field=models.ForeignKey(to='core.Plato', blank=True),
        ),
        migrations.AddField(
            model_name='tablet',
            name='id_mesa',
            field=models.ForeignKey(to='core.Mesa', blank=True),
        ),
    ]
