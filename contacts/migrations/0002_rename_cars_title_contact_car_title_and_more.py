# Generated by Django 4.0.4 on 2022-05-13 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='cars_title',
            new_name='car_title',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='customer_id',
            new_name='customer_need',
        ),
    ]
