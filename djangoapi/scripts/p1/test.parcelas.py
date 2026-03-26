from parcelas.parcelas import ParcelasOOP

# Inicializamos la clase
parcela = ParcelasOOP()

# 1. INSERTAR
datos_nueva = {
    'nombre': 'Parcela de Prueba Forestal',
    'propietario': 'Aserradero y depósito Wilson',
    'area_ha': 45.5,
    'tipo_bosque': 'Pino',
    'estado_legal': 'Propio',
    'perimetro': 950.0,
    'geom': 'POLYGON((2000 2000, 2010 2000, 2010 2010, 2000 2010, 2000 2000))'
}
resultado_insert = parcela.insert(datos_nueva)
print(resultado_insert)

# seguimos con el mismo Id 
if resultado_insert['ok']:
    nuevo_id = resultado_insert['data'][0]['id']
    
    # SELECCIONAR (LEER)
    print("\n- LA PARCELA INSERTADA(select) ")
    print(parcela.selectAsDicts({'id': nuevo_id}))
    
    # ACTUALIZAR
    print("\n-ACTUALIZANDOO...-")
    datos_actualizar = {
        'id': nuevo_id,
        'nombre': 'Parcela de Prueba ACTUALIZADA',
        'propietario': 'Aserradero y depósito Wilson',
        'area_ha': 50.0,
        'tipo_bosque': 'Eucalipto',
        'estado_legal': 'Propio',
        'perimetro': 1200.0,      
        'geom': 'POLYGON((2000 2000, 2010 2000, 2010 2010, 2000 2010, 2000 2000))'
    }
    print(parcela.update(datos_actualizar))
    
    # 4. BORRAR
    #print("\n-Delete(Borrando parcela insertada-)")
    #print(parcela.delete({'id': nuevo_id}))

    