# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150804_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
