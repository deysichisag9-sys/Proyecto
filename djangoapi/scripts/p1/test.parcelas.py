from parcelas.parcelas import Parcelas

# 1. Instanciamos la clase
parcela = Parcelas()

# 2. Creamos el diccionario con los datos de una parcela inventada (un cuadrado simple)
datos_nueva_parcela = {
    'nombre': 'Parcela Norte',
    'propietario': 'Aserradero Wilson',
    'area_ha': 100.5,
    'tipo_bosque': 'Pino y Eucalipto',
    'estado_legal': 'Concesion',
    'geom': 'POLYGON((0 0, 10 0, 10 10, 0 10, 0 0))'
}

print("--- INTENTANDO INSERTAR ---")
resultado_insert = parcela.insert(datos_nueva_parcela)
print(resultado_insert)

# Si se insertó bien, tomamos el ID nuevo y probamos buscarlo
if resultado_insert['ok']:
    nuevo_id = resultado_insert['data'][0]['id']
    
    print("\n--- INTENTANDO SELECCIONAR (SELECT) ---")
    datos_buscar = {'id': nuevo_id}
    print(parcela.selectAsDicts(datos_buscar))
    