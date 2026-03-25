from caminos.camino import Caminos

camino = Caminos()

datos_nuevo_camino = {
    'nombre': 'Ruta Principal de Extraccion',
    'tipo_superficie': 'Tierra compactada',
    'ancho_m': 4.5,
    'estado_mantenimiento': 'Bueno',
    'pendiente_max_pct': 12.5,
    'geom': 'LINESTRING(-5 5, 5 5, 15 5)' # línea que cruza el mapa
}

print("INSERT CAMINO ")
resultado = camino.insert(datos_nuevo_camino)
print(resultado)
