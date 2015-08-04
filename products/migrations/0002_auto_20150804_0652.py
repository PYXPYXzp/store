# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='characteristics',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='specification',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='flower',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='height_shisha',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='type_bowls',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='units',
            field=models.ForeignKey(blank=True, to='products.Units', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight_tobacco',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='type_product',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='units',
            name='type_units',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
