# Generated by Django 4.0.4 on 2022-04-19 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='post',
            name='imagen',
        ),
    ]