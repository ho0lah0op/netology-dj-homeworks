# Generated by Django 4.2.7 on 2023-11-21 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='lte_exist',
            new_name='lte_exists',
        ),
    ]