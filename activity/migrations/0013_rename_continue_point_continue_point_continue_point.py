# Generated by Django 3.2.15 on 2022-10-08 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0012_alter_reward_recieve_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='continue_point',
            old_name='Continue_Point',
            new_name='continue_point',
        ),
    ]
