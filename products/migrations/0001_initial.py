# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('flower', models.CharField(max_length=200)),
                ('weight_tobacco', models.IntegerField(default=0)),
                ('height_shisha', models.IntegerField(default=0)),
                ('type_bowls', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_units', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(to='products.Type'),
        ),
        migrations.AddField(
            model_name='product',
            name='units',
            field=models.ForeignKey(to='products.Units'),
        ),
    ]
