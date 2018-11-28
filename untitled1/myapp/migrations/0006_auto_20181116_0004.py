# Generated by Django 2.1.3 on 2018-11-16 00:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20181115_0249'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RoleCode',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='admin', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='userrole',
            name='dateAssigned',
            field=models.DateField(default=datetime.datetime(2018, 11, 16, 0, 4, 19, 705386)),
        ),
    ]