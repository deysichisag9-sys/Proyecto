from caminos.camino import Caminos

camino = Caminos()

    #  ACTUALIZAR
datos_actualizar = {
      'id' : 7,
    'nombre': 'examen',
    'tipo_superficie': 'Tierra ',
    'ancho_m': 5.5,
    'estado_mantenimiento': 'Bueno',
    'pendiente_max_pct': 12.0,
    'longitud': 1020.2,
    'geom': 'LINESTRING(1000 1000, 1500 1500, 2000 2000)' # 
}
print(camino.update(datos_actualizar))
