from parcelas.parcelasDjango import ParcelasDjango

# Inicializamos la clase
parcela_django = ParcelasDjango()

# 1. INSERT
print("--- 1. INSERTANDO CON DJANGO ---")
datos_nueva_django = {
    'nombre': 'Parcela Django Forestal',
    'propietario': 'Aserradero y depósito Wilson',
    'area_ha': 30.0,
    'tipo_bosque': 'Mixto',
    'estado_legal': 'Concesion',
    'perimetro': 850.5,
    'geom': 'POLYGON((3000 3000, 3010 3000, 3010 3010, 3000 3010, 3000 3000))'
}
resultado_insert_dj = parcela_django.insert(datos_nueva_django)
print(resultado_insert_dj)

if resultado_insert_dj['ok']:
    nuevo_id_dj = resultado_insert_dj['data'][0]['id']
    
    # 2. SELECCIONAR
    print("\n-leyendo-")
    print(parcela_django.selectAsDicts({'id': nuevo_id_dj}))
    
    # 3. ACTUALIZAR
    print("\n-ACTUALIZANDOOOO......-")
    datos_actualizar_dj = {
        'id': nuevo_id_dj,
        'nombre': 'Parcela Django ACTUALIZADA',
        'propietario': 'Aserradero y depósito Wilson',
        'area_ha': 35.0,
        'tipo_bosque': 'Teca', 
        'estado_legal': 'Concesion',
        'perimetro': 900.0,    
        'geom': 'POLYGON((3000 3000, 3010 3000, 3010 3010, 3000 3010, 3000 3000))'
    }
    print(parcela_django.update(datos_actualizar_dj))
    
    # 4. BORRAR
    print("\n- ELIMINANDO- ")
    print(parcela_django.delete({'id': nuevo_id_dj}))

