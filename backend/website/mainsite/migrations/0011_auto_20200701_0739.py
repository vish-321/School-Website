# Generated by Django 3.0.5 on 2020-07-01 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0010_auto_20200701_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='permenant_address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='temporary_address',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
