# Generated by Django 4.0.1 on 2022-03-24 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Indicadores', '0010_remove_tableindi_mes'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableindi',
            name='mes',
            field=models.CharField(default=3, max_length=50),
        ),
    ]
