# Generated by Django 2.2.12 on 2020-07-31 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('mysite', '0027_auto_20200715_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('google', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
    ]
