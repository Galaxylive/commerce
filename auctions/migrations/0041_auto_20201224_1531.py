# Generated by Django 3.1 on 2020-12-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0040_auto_20201224_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='starting_price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
    ]
