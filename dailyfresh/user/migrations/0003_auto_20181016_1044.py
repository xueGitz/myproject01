# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_useraddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='myPhone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='myaddress',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
