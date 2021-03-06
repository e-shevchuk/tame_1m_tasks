# Generated by Django 2.2.12 on 2020-07-06 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0024_googlecreds_creds'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='googlecreds',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='googlecreds',
            name='client_secret',
        ),
        migrations.RemoveField(
            model_name='googlecreds',
            name='expiry',
        ),
        migrations.RemoveField(
            model_name='googlecreds',
            name='id_token',
        ),
        migrations.RemoveField(
            model_name='googlecreds',
            name='refresh_token',
        ),
        migrations.RemoveField(
            model_name='googlecreds',
            name='scopes',
        ),
        migrations.RemoveField(
            model_name='googlecreds',
            name='token',
        ),
        migrations.RemoveField(
            model_name='googlecreds',
            name='token_uri',
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Event')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Task')),
            ],
        ),
    ]
