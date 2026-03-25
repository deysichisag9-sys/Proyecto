import sys
import os
import django

# para ubicar dpnde esta el proyecto 
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
    'geom': 'POINT(25 5)' # Parcela Este 
}

print(" Insert el Arbol con Django")
resultado = arbol_django.insert(datos_nuevo_arbol)
print(resultado)
