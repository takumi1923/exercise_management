# Generated by Django 3.2.15 on 2022-09-28 22:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0008_continue_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward_Recieve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward_recieve_point', models.IntegerField(default=0, verbose_name='ご褒美ポイント')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
