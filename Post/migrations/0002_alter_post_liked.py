# Generated by Django 4.1.1 on 2022-11-22 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_alter_profile_friends'),
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked', to='Home.profile'),
        ),
    ]
