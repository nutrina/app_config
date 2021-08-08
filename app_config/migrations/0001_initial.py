# Generated by Django 3.2.6 on 2021-08-08 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_config.app')),
            ],
        ),
        migrations.CreateModel(
            name='ConfigRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_config.app')),
            ],
        ),
    ]
