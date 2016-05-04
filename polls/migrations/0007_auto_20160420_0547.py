# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 05:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_manager_salesman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='city_name',
            field=models.ForeignKey(db_column='city_name', on_delete=django.db.models.deletion.CASCADE, to='polls.City'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lives_in',
            field=models.ForeignKey(db_column='lives_in', null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.City'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='staff_id',
            field=models.ForeignKey(db_column='staff_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='polls.Staff'),
        ),
        migrations.AlterField(
            model_name='salesman',
            name='staff_id',
            field=models.ForeignKey(db_column='staff_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='polls.Staff'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='manager_id',
            field=models.ForeignKey(db_column='manager_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.Staff'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='works_in',
            field=models.ForeignKey(db_column='works_in', on_delete=django.db.models.deletion.CASCADE, to='polls.Airport'),
        ),
    ]