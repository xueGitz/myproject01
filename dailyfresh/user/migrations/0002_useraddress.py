# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('reciname', models.CharField(verbose_name='收件人', max_length=10)),
                ('address', models.TextField(verbose_name='地址')),
                ('postcode', models.CharField(verbose_name='邮编', max_length=10)),
                ('phoneNum', models.CharField(verbose_name='电话号码', max_length=11)),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'db_table': 'df_user_address',
            },
        ),
    ]
