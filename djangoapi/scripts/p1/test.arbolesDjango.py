import sys
import os
import django

# para ubicar dpnde esta el proyecto 
sys.path.append('/usr/src/app')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoapi.settings")
django.setup()

from arboles.arbolesDjango import ArbolesDjango

arbol_django = ArbolesDjango()

datos_nuevo = {
    'especie': 'eucalipto',
    'diametro_cm': 40.0,
    'altura_m': 20.5,
    'volumen_m3': 1.5,
    'calidad_madera': 'Alta',
    'geom': 'POINT(2005 2005)' # Parcela x mayor 2000 y y menor a 2010 (ojo) interseccion de la parcela 
}
resultado_insert_dj = arbol_django.insert(datos_nuevo)
print(resultado_insert_dj)

if resultado_insert_dj['ok']:
    nuevo_id_dj = resultado_insert_dj['data'][0]['id']
    
    # print("\n-LEYENDO ÁRBOL")
    # print(arbol_django.selectAsDicts({'id': nuevo_id_dj}))
    
    # print("\n-actualizandooo-")
    # datos_actualizar_dj = {
    #     'id': nuevo_id_dj,
    #     'especie': 'Eucalipto Blanco',
    #     'diametro_cm': 35.0,
    #     'altura_m': 22.0,
    #     'volumen_m3': 1.5,
    #     'calidad_madera': 'Alta',
    #     'geom': 'POINT(6000 6000)'
    # }
    # print(arbol_django.update(datos_actualizar_dj))
    
    # print("\n-Eliminado-")
    # print(arbol_django.delete({'id': nuevo_id_dj}))
