# Generated by Django 4.0.3 on 2022-03-17 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='clasificacion',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='nombre_categoria',
            new_name='subCategoria',
        ),
    ]