# Generated by Django 2.2.12 on 2020-07-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0019_auto_20200703_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='googlecreds',
            name='expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]