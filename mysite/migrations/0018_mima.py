# Generated by Django 2.2.12 on 2020-07-03 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('mysite', '0017_event_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='MIMA',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('google_auth_creds', models.CharField(blank=True, default='', max_length=1000, null=True)),
            ],
        ),
    ]
