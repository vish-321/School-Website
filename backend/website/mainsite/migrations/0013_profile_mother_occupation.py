# Generated by Django 3.0.5 on 2020-07-01 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0012_profile_student_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mother_occupation',
            field=models.CharField(default='', max_length=20),
        ),
    ]
