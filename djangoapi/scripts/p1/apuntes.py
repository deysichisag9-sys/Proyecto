#INSERT

from arboles.arboles import ArbolesOOP
arbol = ArbolesOOP()

print("--- INSERTANDO ÁRBOL (SQL) ---")
datos = {
    'especie': 'Pino Radiata',
    'diametro_cm': 45.5,
    'altura_m': 18.2,
    'estado_sanitario': 'Sano',
    'geom': 'POINT(505 505)' # Cae dentro de la parcela 
}
print(arbol.insert(datos))
#-----------------
#Arboles SELECT
from arboles.arboles import ArbolesOOP
arbol = ArbolesOOP()

print("--- LEYENDO ÁRBOL (SQL) ---")
print(arbol.selectAsDicts({'id': 1})) # Cambia el 1 por el ID real

#----------
#UPDATE 
from arboles.arboles import ArbolesOOP
arbol = ArbolesOOP()

print("--- ACTUALIZANDO ÁRBOL (SQL) ---")
datos = {
    'id': 1, # Cambia el 1 por el ID real
    'especie': 'Pino Radiata',
    'diametro_cm': 50.0, # Creció
    'altura_m': 20.0,    # Creció
    'estado_sanitario': 'Sano',
    'geom': 'POINT(505 505)'
}
print(arbol.update(datos))

#----------
#DELETE 
from arboles.arboles import ArbolesOOP
arbol = ArbolesOOP()

print("--- BORRANDO ÁRBOL (SQL) ---")
print(arbol.delete({'id': 1})) # Cambia el 1 por el ID real

#--------DJANGO------
#ÁRBOLES - DJANGO ORM

from arboles.arbolesDjango import ArbolesDjango
arbol_dj = ArbolesDjango()

print("--- INSERTANDO ÁRBOL (DJANGO) ---")
datos = {
    'especie': 'Eucalipto Blanco',
    'diametro_cm': 35.0,
    'altura_m': 22.0,
    'estado_sanitario': 'Observacion',
    'geom': 'POINT(3005 3005)'
}
print(arbol_dj.insert(datos))

#-------------------
#SELECT 
from arboles.arbolesDjango import ArbolesDjango
arbol_dj = ArbolesDjango()

print("--- LEYENDO ÁRBOL (DJANGO) ---")
print(arbol_dj.selectAsDicts({'id': 1}))

#---------
#UPDATE 
from arboles.arbolesDjango import ArbolesDjango
arbol_dj = ArbolesDjango()

print("--- ACTUALIZANDO ÁRBOL (DJANGO) ---")
datos = {
    'id': 1,
    'especie': 'Eucalipto Blanco',
    'diametro_cm': 35.0,
    'altura_m': 22.0,
    'estado_sanitario': 'Sano', # Curado
    'geom': 'POINT(3005 3005)'
}
print(arbol_dj.update(datos))

#------------------------------
#DELETE

from arboles.arbolesDjango import ArbolesDjango
arbol_dj = ArbolesDjango()

print("--- BORRANDO ÁRBOL (DJANGO) ---")
print(arbol_dj.delete({'id': 1}))

#PYSOPG 
#-----------------------
from caminos.camino import CaminosOOP
camino = CaminosOOP()

print("--- INSERTANDO CAMINO (SQL) ---")
datos = {
    'nombre': 'Vía Principal',
    'tipo_superficie': 'Tierra',
    'ancho_m': 6.5,
    'estado_mantenimiento': 'Bueno',
    'pendiente_max_pct': 12.0,
    'longitud': 1500.5,
    'geom': 'LINESTRING(100 100, 200 200, 300 300)'
}
print(camino.insert(datos))

#-------
#SELECT 
from caminos.camino import CaminosOOP
camino = CaminosOOP()

print("--- LEYENDO CAMINO (SQL) ---")
print(camino.selectAsDicts({'id': 1}))

#-------------
#UPDATE 
from caminos.camino import CaminosOOP
camino = CaminosOOP()

print("--- ACTUALIZANDO CAMINO (SQL) ---")
datos = {
    'id': 1,
    'nombre': 'Vía Principal',
    'tipo_superficie': 'Grava', # Mejorado
    'ancho_m': 7.0,             # Ensanchado
    'estado_mantenimiento': 'Excelente',
    'pendiente_max_pct': 12.0,
    'longitud': 1500.5,
    'geom': 'LINESTRING(100 100, 200 200, 300 300)'
}
print(camino.update(datos))

#-----------------------
#DELETE
from caminos.camino import CaminosOOP
camino = CaminosOOP()

print("--- BORRANDO CAMINO (SQL) ---")
print(camino.delete({'id': 1}))

#---------------DJANGO-------
#INSERT 
from caminos.caminosDjango import CaminosDjango
camino_dj = CaminosDjango()

print("--- INSERTANDO CAMINO (DJANGO) ---")
datos = {
    'nombre': 'Sendero Secundario',
    'tipo_superficie': 'Arcilla',
    'ancho_m': 4.0,
    'estado_mantenimiento': 'Regular',
    'pendiente_max_pct': 15.5,
    'longitud': 850.0,
    'geom': 'LINESTRING(400 400, 450 450)'
}
print(camino_dj.insert(datos))

#---------- 
#SELECT
from caminos.caminosDjango import CaminosDjango
camino_dj = CaminosDjango()

print("--- LEYENDO CAMINO (DJANGO) ---")
print(camino_dj.selectAsDicts({'id': 1}))

#---------
#UPATE (ACTUALIZAR)
from caminos.caminosDjango import CaminosDjango
camino_dj = CaminosDjango()

print("--- ACTUALIZANDO CAMINO (DJANGO) ---")
datos = {
    'id': 1,
    'nombre': 'Sendero Secundario',
    'tipo_superficie': 'Arcilla',
    'ancho_m': 4.0,
    'estado_mantenimiento': 'Malo', # Dañado
    'pendiente_max_pct': 15.5,
    'longitud': 850.0,
    'geom': 'LINESTRING(400 400, 450 450)'
}
print(camino_dj.update(datos))

#----- 
#DELETE
from caminos.caminosDjango import CaminosDjango
camino_dj = CaminosDjango()

print("--- BORRANDO CAMINO (DJANGO) ---")
print(camino_dj.delete({'id': 1}))

#IMPORTANTE OBSERVAR EL NUMERO DEL ID 

#------PSYCOPG 
#------ INSERT 
from parcelas.parcelas import ParcelasOOP
parcela = ParcelasOOP()

print("--- INSERTANDO PARCELA (SQL) ---")
datos = {
    'nombre': 'Parcela Norte',
    'propietario': 'Aserradero y deposito Wilson',
    'area_ha': 20.0,
    'tipo_bosque': 'Pino',
    'estado_legal': 'Propio',
    'perimetro': 800.0,
    'geom': 'POLYGON((500 500, 510 500, 510 510, 500 510, 500 500))'
}
print(parcela.insert(datos))

#--------
#SELECT 
from parcelas.parcelas import ParcelasOOP
parcela = ParcelasOOP()

print("--- LEYENDO PARCELA (SQL) ---")
print(parcela.selectAsDicts({'id': 1})) # Cambia el 1 por el ID real

#------ 
#UPDATE 
from parcelas.parcelas import ParcelasOOP
parcela = ParcelasOOP()

print("--- ACTUALIZANDO PARCELA (SQL) ---")
datos = {
    'id': 1, # Cambia el 1 por el ID real
    'nombre': 'Parcela Norte (Ampliación)',
    'propietario': 'Aserradero y deposito Wilson',
    'area_ha': 25.0, # Modificado
    'tipo_bosque': 'Pino',
    'estado_legal': 'Propio',
    'perimetro': 950.0, # Modificado
    'geom': 'POLYGON((500 500, 510 500, 510 510, 500 510, 500 500))'
}
print(parcela.update(datos))

#------ 
#DELETE / BOORAR 
from parcelas.parcelas import ParcelasOOP
parcela = ParcelasOOP()

print("--- BORRANDO PARCELA (SQL) ---")
print(parcela.delete({'id': 1})) # Cambia el 1 por el ID real


#----- DJANGO 
#INSERT 
from parcelas.parcelasDjango import ParcelasDjango
parcela_dj = ParcelasDjango()

print("--- INSERTANDO PARCELA (DJANGO) ---")
datos = {
    'nombre': 'Parcela Sur',
    'propietario': 'Aserradero y deposito Wilson',
    'area_ha': 15.0,
    'tipo_bosque': 'Eucalipto',
    'estado_legal': 'Concesion',
    'perimetro': 600.0,
    'geom': 'POLYGON((3000 3000, 3010 3000, 3010 3010, 3000 3010, 3000 3000))'
}
print(parcela_dj.insert(datos))

#-------------
#SELECT 
from parcelas.parcelasDjango import ParcelasDjango
parcela_dj = ParcelasDjango()

print("--- LEYENDO PARCELA (DJANGO) ---")
print(parcela_dj.selectAsDicts({'id': 1})) # Cambia el 1 por el ID real

#-------------------
#UPDATE /ACTUALIZAR 
from parcelas.parcelasDjango import ParcelasDjango
parcela_dj = ParcelasDjango()

print("--- ACTUALIZANDO PARCELA (DJANGO) ---")
datos = {
    'id': 1, # Cambia el 1 por el ID real
    'nombre': 'Parcela Sur (Revisada)',
    'propietario': 'Aserradero y deposito Wilson',
    'area_ha': 15.0,
    'tipo_bosque': 'Mixto', # Modificado
    'estado_legal': 'Concesion',
    'perimetro': 600.0,
    'geom': 'POLYGON((3000 3000, 3010 3000, 3010 3010, 3000 3010, 3000 3000))'
}
print(parcela_dj.update(datos))

#------------------
#DELETE
from parcelas.parcelasDjango import ParcelasDjango
parcela_dj = ParcelasDjango()

print("--- BORRANDO PARCELA (DJANGO) ---")
print(parcela_dj.delete({'id': 1})) # Cambia el 1 por el ID real
