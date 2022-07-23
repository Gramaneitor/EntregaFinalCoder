# Generated by Django 4.0.4 on 2022-05-03 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0002_nuestrouser_bio_nuestrouser_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nuestrouser',
            name='bio',
            field=models.TextField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='nuestrouser',
            name='imagen',
            field=models.ImageField(null=True, upload_to='avatares'),
        ),
    ]