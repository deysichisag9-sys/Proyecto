from django.db import models
from django.contrib.gis.db import models as gis_models
import django.utils.timezone as djangoTimezone

# Create your models here.
class Buildings(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    perimeter = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    geom = gis_models.PolygonField(srid=25830,blank=True, null=True) 
    data_creation = models.DateTimeField(blank = True, db_default=djangoTimezone.now())

    def save(self, *args, **kwargs):
            # Calculate values from the geometry before saving
            if self.geom:
                self.area = self.geom.area
                self.perimeter = self.geom.length
            
            super().save(*args, **kwargs)
            

 #Moleds Forestry 
class Parcelas(models.Model):
    nombre = models.CharField(max_length=100)
    propietario = models.CharField(max_length=100)
    area_ha = models.FloatField()
    tipo_bosque = models.CharField(max_length=100)
    perimetro = models.FloatField(null=True, blank=True)
    estado_legal = models.CharField(max_length=50)
    # Usamos gis_modls
    geom = gis_models.PolygonField(srid=25830) 

    class Meta:
        db_table = '"d"."parcelas"' # Se señala  a la tabla en el esquema d
        # es para djgano no cree la tabla, por que ya existe. 
        managed = False 

class Arboles(models.Model):
    especie = models.CharField(max_length=100)
    diametro_cm = models.FloatField()
    altura_m = models.FloatField()
    volumen_m3 = models.FloatField()
    calidad_madera = models.CharField(max_length=50)
    geom = gis_models.PointField(srid=25830)

    class Meta:
        db_table = '"d"."arboles"'
        managed = False

class Caminos(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_superficie = models.CharField(max_length=50)
    ancho_m = models.FloatField()
    estado_mantenimiento = models.CharField(max_length=50)
    pendiente_max_pct = models.FloatField()
    longitud = models.FloatField(null=True, blank=True)
    geom = gis_models.LineStringField(srid=25830)

    class Meta:
        db_table = '"d"."caminos"'
        managed = False         
