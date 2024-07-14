from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categorias = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    # Otros campos necesarios

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    # Otros campos necesarios

    def __str__(self):
        return self.nombre