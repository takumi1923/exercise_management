# Generated by Django 3.2.15 on 2022-10-04 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0011_alter_reward_recieve_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward_recieve',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
