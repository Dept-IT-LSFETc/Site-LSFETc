# Generated by Django 5.1.6 on 2025-03-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DespreNoi', '0003_alter_desprenoi_bc_biroul_executiv_poza_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desprenoi_BC_PozaCoperta_si_text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('an', models.TextField(null=True)),
                ('poza', models.ImageField(null=True, upload_to='desprenoi/poza')),
            ],
        ),
    ]
