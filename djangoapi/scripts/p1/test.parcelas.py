from parcelas.parcelas import  ParcelasOOP

# la clase parcela 
parcela = ParcelasOOP()

# Creacion del diccionario 
datos_nueva_parcela = {
    'nombre': 'Parcela Norte',
    'propietario': 'Aserradero Wilson',
    'area_ha': 100.5,
    'tipo_bosque': 'Pino y Eucalipto',
    'estado_legal': 'Concesion',
    'geom': 'POLYGON((0 0, 10 0, 10 10, 0 10, 0 0))'
}

print("insert ")
resultado_insert = parcela.insert(datos_nueva_parcela)
print(resultado_insert)

# si el insert funciona con siguiente paso el ID nuevo 
if resultado_insert['ok']:
    nuevo_id = resultado_insert['data'][0]['id']
    
    print("\n-Intentando seleccionar -")
    datos_buscar = {'id': nuevo_id}
    print(parcela.selectAsDicts(datos_buscar))
    