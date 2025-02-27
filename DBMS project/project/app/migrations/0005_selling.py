# Generated by Django 5.0.6 on 2024-05-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_fuel_type_sell_carfuel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_name', models.CharField(max_length=100)),
                ('manufacture_year', models.PositiveIntegerField()),
                ('number_of_seats', models.PositiveIntegerField()),
                ('fuel_type', models.CharField(max_length=10)),
                ('mileage', models.PositiveIntegerField()),
                ('quote_price', models.PositiveIntegerField()),
            ],
        ),
    ]
