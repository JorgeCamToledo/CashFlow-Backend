# Generated by Django 4.0.3 on 2023-01-07 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Indicadores', '0011_tableindi_mes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableindi',
            name='mes',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
