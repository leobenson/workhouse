# Generated by Django 4.2.1 on 2023-07-17 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job_post',
            old_name='user_id',
            new_name='user',
        ),
    ]
