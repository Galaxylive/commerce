# Generated by Django 3.1 on 2020-12-07 12:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auto_20201207_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watcher',
            field=models.ManyToManyField(blank=True, related_name='user_watching', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]
