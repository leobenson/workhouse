# Generated by Django 4.2.1 on 2023-08-16 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(default='pending', max_length=150)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.job_post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.worker')),
            ],
        ),
    ]
