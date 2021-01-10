# Generated by Django 3.1 on 2020-12-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20201206_0308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='listings',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='listings',
            field=models.ManyToManyField(null=True, to='auctions.Listing'),
        ),
    ]
