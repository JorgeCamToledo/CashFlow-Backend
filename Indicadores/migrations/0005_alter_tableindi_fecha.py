# Generated by Django 4.0.3 on 2022-03-20 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Indicadores', '0004_tableindi_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableindi',
            name='fecha',
            field=models.DateField(),
        ),
    ]
