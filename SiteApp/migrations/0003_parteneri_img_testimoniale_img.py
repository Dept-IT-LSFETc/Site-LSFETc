# Generated by Django 5.1.6 on 2025-02-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0002_parteneri'),
    ]

    operations = [
        migrations.AddField(
            model_name='parteneri',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Parteneri'),
        ),
        migrations.AddField(
            model_name='testimoniale',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='pozeTestimoniale'),
        ),
    ]
