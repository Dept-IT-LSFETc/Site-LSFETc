# Generated by Django 5.1.6 on 2025-03-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0013_numere'),
    ]

    operations = [
        migrations.AddField(
            model_name='numere',
            name='index',
            field=models.IntegerField(default=0),
        ),
    ]
