from django.db import models

# LANDING PAGE CLASSES

class Pagina_Principala_PozaPrincipala(models.Model):
    img = models.ImageField(null=True,blank=True)
    index = models.IntegerField(default=0)

class Pagina_Principala_OrganizatiiPartenere(models.Model):
    img = models.ImageField(null=True, blank=True)
    nume = models.TextField(null=True)
    link = models.TextField(null=True)
    alt = models.TextField(null=True)
    site= models.TextField(null=True)
    index = models.IntegerField(default=0)

class Pagina_Principala_Testimoniale(models.Model):
    img = models.ImageField(null=True, blank=True)
    title = models.TextField(null=True)
    index = models.IntegerField(default=0)

class Pagina_Principala_Numere(models.Model):
    title = models.CharField(null=True,max_length=255)
    numar = models.CharField(null=True,max_length=255)
    index = models.IntegerField(default=0)

class Contact_Persoane_de_contact(models.Model):
     nume = models.CharField(null= True, max_length= 255)
     functia = models.TextField(null=True)
     numar_de_telefon = models.TextField(default=0)
     email = models.TextField(null=True)
     index = models.IntegerField(default=0)


    
def __str__(self):
    return self.title