# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_delivery', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_order', models.DateTimeField(verbose_name=b'date published')),
                ('total_cost', models.IntegerField(default=0, null=True, blank=True)),
                ('delivery', models.ForeignKey(to='order.Delivery')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200, null=True, blank=True)),
                ('last_name', models.CharField(max_length=200, null=True, blank=True)),
                ('tel_namb', models.IntegerField(default=0, null=True, blank=True)),
                ('city', models.CharField(max_length=200, null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='person',
            field=models.ForeignKey(to='order.Person'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(to='products.Product'),
        ),
    ]
