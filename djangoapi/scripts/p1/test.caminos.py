from caminos.camino import Caminos

camino = Caminos()

datos_nuevo_camino = {
    'nombre': 'Via principal',
    'tipo_superficie': 'Tierra ',
    'ancho_m': 5.5,
    'estado_mantenimiento': 'Bueno',
    'pendiente_max_pct': 12.0,
    'longitud': 1020.2,
    'geom': 'LINESTRING(1000 1000, 1500 1500, 2000 2000)' # 
}


resultado_insert = camino.insert(datos_nuevo_camino)
print(resultado_insert)

if resultado_insert['ok']:
    nuevo_id = resultado_insert['data'][0]['id']
    
    #  SELECCIONAR
    print("\n- LEYENDO CAMINO -")
    print(camino.selectAsDicts({'id': nuevo_id}))
    
    #  ACTUALIZAR
    print("\n-ACTUALIZANDO CAMINO -")
    datos_actualizar = {
        'id': nuevo_id,
        'nombre': 'Vía Principal Maderera (Ampliación)',
        'tipo_superficie': 'examen ', 
        'ancho_m': 8.0,             
        'estado_mantenimiento': 'Excelente',
        'pendiente_max_pct': 12.0,
        'longitud': 1500.5,
        'geom': 'LINESTRING(1000 1000, 1500 1500, 2000 2000)'
    }
    print(camino.update(datos_actualizar))
    
    # BORRAR
    #print("\n-DELETE-")
    #print(camino.delete({'id': nuevo_id}))
    