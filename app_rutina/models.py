"""
? ARCHIVO ORIGINAL CREADO POR STARTAPP DJANGO:
crear clases / tablas sql con ayuda del ORM en archivos migrations en carpeta migrations """

from django.db import models

# Create your models here.

"""
? se crea clase tiene parámetros/hereda modelos de djando, que llama a clase model
. ya es tabla/clase/modelo con 2 columnas (id, nombre)
. SQL permite especificar el tipo de dato
. __str__ metodo/función permite mostrar algo a la interfaz / proporciona una representación en forma de cadena personalizada del objeto de la clase que muestra el valor del atributo  """
class t_cuerpo (models.Model):

    cuerpo = models.CharField(max_length=200)

    def __str__ (self):
        return self.nombre


"""
? foreignkey = esta tabla tiene relacion con otra tabla y lo relaciona con ids
. 'on_delete = models.CASCADE': si se elimine elemento de tabla asociada, se elimina todos los elementos de esta tabla 
. puedo hacer actualizaciones de columnas a las tablas cuando necesite, sin olvidar migrar
. puedo cambiarle el nombre a las tablas y columnas, cambiando todas las referencias, migrando y aceptando los cambios en la terminal del ORM, los archivos migration se referencian en cadena si alguno de la cadena esta erroneo ni te cuento carnal
. no se por que no respeta el orden de aparicion de las columnas en la base de datos """
class t_ejercicio (models.Model):

    cuerpo = models.ForeignKey(t_cuerpo,on_delete=models.CASCADE)
    ejercicio = models.CharField(max_length=200)
    posicion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    repeticiones = models.IntegerField()

    def __str__ (self):
        return self.nombre
