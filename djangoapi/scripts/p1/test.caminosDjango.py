import sys
import os
import django

# path proyecto la ubicacion 
sys.path.append('/usr/src/app')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoapi.settings")
django.setup()

from caminos.caminosDjango import CaminosDjango

camino_django = CaminosDjango()

datos_nuevo_camino = {
    'nombre': 'Ruta Secundaria',
    'tipo_superficie': 'Arcilla',
    'ancho_m': 4.0,
    'estado_mantenimiento': 'Regular',
    'pendiente_max_pct': 10.5,
    'longitud': 850.2,
    'geom': 'LINESTRING(3000 3000, 3500 3500)' # Una línea que cruza por el mapa
}

resultado = camino_django.insert(datos_nuevo_camino)
print(resultado)

if resultado['ok']:
    nuevo_id_dj = resultado['data'][0]['id']
    
    print("\n-leyendo camino -")
    print(camino_django.selectAsDicts({'id': nuevo_id_dj}))
    
    print("\n-actualizando-")
    datos_actualizar_dj = {
        'id': nuevo_id_dj,
        'nombre': 'Sendero Secundario Wilson',
        'tipo_superficie': 'Arcilla',
        'ancho_m': 4.0,
        'estado_mantenimiento': 'Malo', 
        'pendiente_max_pct': 15.5,
        'longitud': 850.0,
        'geom': 'LINESTRING(3000 3000, 3500 3500)'
    }
    print(camino_django.update(datos_actualizar_dj))
    
    print("\n- DELETE CAMINO -")
    print(camino_django.delete({'id': nuevo_id_dj}))
