# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('uname', models.CharField(unique=True, max_length=10)),
                ('upwd', models.CharField(max_length=20)),
                ('uemail', models.CharField(unique=True, max_length=50)),
                ('isdelete', models.BooleanField(default=False)),
            ],
        ),
    ]
