from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Kotxea(models.Model):
    matrikula = models.CharField(max_length=50, primary_key=True)
    marka = models.CharField(max_length=100)
    prezioa = models.DecimalField(max_digits=8, decimal_places=2, validators=[
        MinValueValidator(0)])

    def __str__(self):
        return self.marka


class Bezeroa(models.Model):
    dni = models.CharField(max_length=50,primary_key=True)
    izena = models.CharField(max_length=50)
    abizena = models.CharField(max_length=50)
    adina = models.IntegerField(validators=[
        MinValueValidator(0)])

    def __str__(self):
        return self.izena


class Alokairua(models.Model):
    kotxe_matrikula = models.ForeignKey(Kotxea, on_delete=models.CASCADE)
    bezero_dni = models.ForeignKey(Bezeroa, on_delete=models.CASCADE)
    alokairu_data_hasi = models.DateField(null=True)
    alokairu_data_bukatu = models.DateField(null=True)