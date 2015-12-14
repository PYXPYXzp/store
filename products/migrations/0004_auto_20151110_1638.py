# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bal_program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bal', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_company', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(blank=True, to='products.Company', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(blank=True, to='products.Type', null=True),
        ),
    ]
