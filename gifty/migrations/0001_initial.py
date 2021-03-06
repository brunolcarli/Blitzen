# Generated by Django 2.2.10 on 2020-11-26 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FederalPublicUtilityCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=15)),
                ('mj_process', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='MunicipalPublicUtilityCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=15)),
                ('mj_process', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Ong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_contact', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StatePublicUtilityCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=15)),
                ('mj_process', models.CharField(max_length=15)),
            ],
        ),
    ]
