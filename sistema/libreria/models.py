from django.db import models

class libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Titulo')
    imagen=models.ImageField(upload_to='imagenes/',verbose_name='imagen',null=True)
    descripcion=models.TextField(verbose_name='Descripcion',null=True)
    
    
    

# Create your models here.
