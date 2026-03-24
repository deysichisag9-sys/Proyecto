# Para que Django funcione en un script suelto, necesitamos estas 3 líneas primero:
import os
import django
import sys

sys.path.append('/usr/src/app')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoapi.settings")
django.setup()

# Ahora sí, importamos tu nueva clase
from parcelas.parcelasDjango import ParcelasDjango

parcela_django = ParcelasDjango()

datos_nueva_parcela = {
    'nombre': 'Parcela Este',
    'propietario': 'Aserradero Wilson',
    'area_ha': 75.0,
    'tipo_bosque': 'Eucalipto',
    'estado_legal': 'Propio',
    'geom': 'POLYGON((20 0, 30 0, 30 10, 20 10, 20 0))' # Un polígono nuevo que no choca
}

print("--- INTENTANDO INSERTAR CON DJANGO ---")
resultado = parcela_django.insert(datos_nueva_parcela)
print(resultado)
