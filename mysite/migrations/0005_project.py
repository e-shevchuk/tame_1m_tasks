# Generated by Django 2.2.12 on 2020-06-11 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_task_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
