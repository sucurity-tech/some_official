# Generated by Django 4.1.1 on 2022-11-20 03:33

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_relationship'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='relationship',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
