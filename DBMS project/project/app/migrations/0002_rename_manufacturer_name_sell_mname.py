# Generated by Django 5.0.6 on 2024-05-28 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sell',
            old_name='manufacturer_name',
            new_name='mname',
        ),
    ]
