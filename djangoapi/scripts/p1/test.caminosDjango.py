import sys
import os
import django

# Le enseñamos a Python dónde está el proyecto
sys.path.append('/usr/src/app')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoapi.settings")
django.setup()

from caminos.caminosDjango import CaminosDjango

camino_django = CaminosDjango()

datos_nuevo_camino = {
    'nombre': 'Ruta Extraccion Aserradero',
    'tipo_superficie': 'Grava',
    'ancho_m': 5.0,
    'estado_mantenimiento': 'Regular',
    'pendiente_max_pct': 8.5,
    'geom': 'LINESTRING(15 5, 25 5, 35 5)' # Una línea que cruza por el mapa
}

print("--- INTENTANDO INSERTAR CAMINO CON DJANGO ---")
resultado = camino_django.insert(datos_nuevo_camino)
print(resultado)
