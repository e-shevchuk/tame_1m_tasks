# Generated by Django 2.2.12 on 2020-06-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20200617_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]