# Generated by Django 4.0.5 on 2022-07-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0004_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('Dulce', 'Dulce'), ('Salado', 'Salado'), ('Vegetariano', 'Vegetariano'), ('Desayunos', 'Desayunos'), ('Sopas', 'Sopas')], default=1, max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='ingredientes',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]