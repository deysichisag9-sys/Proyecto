import sys
import os
import django

# Le enseñamos a Python dónde está el proyecto
sys.path.append('/usr/src/app')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoapi.settings")
django.setup()

from arboles.arbolesDjango import ArbolesDjango

arbol_django = ArbolesDjango()

datos_nuevo_arbol = {
    'especie': 'Pino Radiata',
    'diametro_cm': 40.0,
    'altura_m': 20.5,
    'volumen_m3': 1.5,
    'calidad_madera': 'Alta',
    'geom': 'POINT(25 5)' # ¡Cae justo dentro de la Parcela Este!
}

print("--- INTENTANDO INSERTAR ARBOL CON DJANGO ---")
resultado = arbol_django.insert(datos_nuevo_arbol)
print(resultado)
