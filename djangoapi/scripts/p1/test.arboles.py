from arboles.arboles import Arboles

arbol = Arboles()

datos_nuevo = {
    'especie': 'Pino Radiata',
    'diametro_cm': 45.5,
    'altura_m': 20.3,
    'volumen_m3': 1.8,
    'calidad_madera': 'buena',
    'geom': 'POINT(5000 5000)' #parcela(norte)
}

resultado_insert = arbol.insert(datos_nuevo)
print(resultado_insert)

if resultado_insert['ok']:
    nuevo_id = resultado_insert['data'][0]['id']
    
    print("\n-leyendo arbol-")
    print(arbol.selectAsDicts({'id': nuevo_id}))
    
    print("\n- actualizando datos -")
    datos_actualizar = {
        'id': nuevo_id,
        'especie': 'Pino Radiata',
        'diametro_cm': 48.0,          
        'altura_m': 19.5,            
        'volumen_m3': 2.3,
        'calidad_madera': 'excelente',
        'geom': 'POINT(5000 5000)'
    }
    print(arbol.update(datos_actualizar))
    
    print("\n-DELETE (Eliminado)")
    print(arbol.delete({'id': nuevo_id}))
    
    
