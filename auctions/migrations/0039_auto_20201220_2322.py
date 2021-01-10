# Generated by Django 3.1 on 2020-12-20 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0038_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='description',
            new_name='content',
        ),
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
