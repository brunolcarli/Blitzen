# Generated by Django 2.2.10 on 2020-12-01 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifty', '0003_auto_20201128_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ong',
            name='cnas',
        ),
    ]
