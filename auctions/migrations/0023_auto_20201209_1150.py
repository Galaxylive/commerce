# Generated by Django 3.1 on 2020-12-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20201207_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to='auctions.Listing'),
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]
