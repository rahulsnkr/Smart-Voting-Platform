# Generated by Django 2.1.2 on 2018-10-21 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0006_remove_voter_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='username',
            field=models.OneToOneField(db_column='username', on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]