# Generated by Django 4.2.1 on 2023-07-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_job_post_expected_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]