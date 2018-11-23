# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20181016_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaContect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tittle', models.CharField(verbose_name='地区', max_length=20)),
                ('parent', models.ForeignKey(null=True, to='user.AreaContect', blank=True)),
            ],
        ),
    ]
