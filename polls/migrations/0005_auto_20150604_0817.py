# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150604_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='category',
            field=models.CharField(choices=[('DEM', 'Demographics'), ('POL', 'Politics'), ('SPRT', 'Sports'), ('TECH', 'Technology'), ('AC', 'Academics'), ('TRVL', 'Travel')], verbose_name='poll category', max_length=64),
        ),
    ]
