# Generated by Django 3.1 on 2020-12-04 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_ending_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='ending_price',
        ),
    ]
