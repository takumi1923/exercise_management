# Generated by Django 3.2.15 on 2022-10-24 12:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0031_point_amari'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewardtake',
            name='point',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='ご褒美に使用するポイント'),
        ),
    ]
