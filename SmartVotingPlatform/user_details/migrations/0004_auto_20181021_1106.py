# Generated by Django 2.1.2 on 2018-10-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0003_auto_20181020_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='voter',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
