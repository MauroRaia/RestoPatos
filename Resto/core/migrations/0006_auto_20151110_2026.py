# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151110_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('estados', models.CharField(default=b'Pedido', max_length=1, choices=[(b'El plato esta por ser elaborado', b'Ordenado'), (b'Elaborando el plato', b'Cocinando'), (b'Plato cobrado', b'Pagado')])),
            ],
        ),
        migrations.CreateModel(
            name='Valoracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('valor_plato', models.DecimalField(default=0.0, max_digits=2, decimal_places=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='consumo',
            name='seccion_consumo',
        ),
        migrations.RemoveField(
            model_name='carta',
            name='pedidos_actuales',
        ),
        migrations.RemoveField(
            model_name='mesa',
            name='pedidos',
        ),
        migrations.RemoveField(
            model_name='seccion',
            name='items',
        ),
        migrations.AddField(
            model_name='bebida',
            name='seccion_bebida',
            field=models.ForeignKey(to='core.Seccion', null=True),
        ),
        migrations.AddField(
            model_name='plato',
            name='seccion_platos',
            field=models.ForeignKey(to='core.Seccion', null=True),
        ),
        migrations.AddField(
            model_name='plato',
            name='valor_total',
            field=models.DecimalField(default=0.0, max_digits=2, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='carta',
            name='seccion_actual',
            field=models.ForeignKey(blank=True, to='core.Seccion', null=True),
        ),
        migrations.DeleteModel(
            name='Consumo',
        ),
        migrations.AddField(
            model_name='valoracion',
            name='plato_valorado',
            field=models.ForeignKey(to='core.Plato'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='mesa',
            field=models.ForeignKey(to='core.Mesa'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='platos',
            field=models.ForeignKey(to='core.Plato'),
        ),
    ]
