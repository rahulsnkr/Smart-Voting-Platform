# Generated by Django 2.1.2 on 2018-10-20 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='voter',
            name='email',
        ),
    ]