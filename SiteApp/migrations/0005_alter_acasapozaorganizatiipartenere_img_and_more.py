# Generated by Django 5.1.6 on 2025-03-05 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0004_acasapozaorganizatiipartenere_acasapozaprincipala_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acasapozaorganizatiipartenere',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='SiteApp/static/poze/acasa/pozaOrganizatiiPartenere'),
        ),
        migrations.AlterField(
            model_name='acasapozaprincipala',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='SiteApp/static/poze/acasa/PozaPrincipala'),
        ),
    ]
