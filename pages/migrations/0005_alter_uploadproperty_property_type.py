# Generated by Django 4.0.4 on 2022-05-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200206_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadproperty',
            name='property_type',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Rent', 'Rent')], max_length=10),
        ),
    ]
