# Generated by Django 3.2.15 on 2022-09-18 12:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateField(verbose_name='日付')),
                ('start_time', models.TimeField(default=datetime.time(7, 0), verbose_name='開始時間')),
                ('excercise_time', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.list')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
