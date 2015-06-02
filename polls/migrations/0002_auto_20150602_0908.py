# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='poll',
            field=models.ForeignKey(blank=True, to='polls.Poll', null=True, verbose_name='poll question'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='category',
            field=models.CharField(choices=[('DEM', 'Demographics'), ('POL', 'Politics'), ('SPT', 'Sports'), ('TEC', 'Technology'), ('ACD', 'Academics'), ('TRL', 'Travel')], verbose_name='poll category', max_length=64),
        ),
    ]
