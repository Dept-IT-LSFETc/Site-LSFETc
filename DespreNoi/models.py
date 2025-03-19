from django.db import models


class Desprenoi_BC_PozaCoperta_si_text(models.Model):
    title = models.CharField(max_length=255)
    an = models.TextField(null=True)
    poza = models.ImageField(null=True,upload_to='desprenoi/poza')

class Desprenoi_BC_Biroul_executiv(models.Model):
    title = models.CharField(max_length=255)
    poza = models.ImageField(null=True, upload_to='desprenoi/bc/bex')
    nume = models.TextField(null=True)
    functia = models.TextField(null=True)
    link_facebook = models.TextField(null=True)
    link_instagram = models.TextField(null=True)
    index = models.IntegerField(default=0)


class Desprenoi_BC_Coordonatori_Departamente(models.Model):
    title = models.CharField(max_length=255)
    poza = models.ImageField(null=True, upload_to='desprenoi/bc/bc')
    nume = models.TextField(null=True)
    functia = models.TextField(null=True)
    link_facebook = models.TextField(null=True)
    link_instagram = models.TextField(null=True)
    index = models.IntegerField(default=0)


class Desprenoi_BC_Comisia_de_cenzori(models.Model):
    title = models.CharField(max_length=255)
    poza = models.ImageField(null=True, upload_to='desprenoi/bc/cc')
    nume = models.TextField(null=True)
    functia = models.TextField(null=True)
    link_facebook = models.TextField(null=True)
    link_instagram = models.TextField(null=True)
    index = models.IntegerField(default=0)

# Create your models here.
