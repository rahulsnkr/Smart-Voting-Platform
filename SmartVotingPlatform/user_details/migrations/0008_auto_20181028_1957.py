# Generated by Django 2.1.2 on 2018-10-28 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0007_auto_20181021_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partypolicies',
            name='policies',
            field=models.CharField(max_length=1000),
        ),
    ]