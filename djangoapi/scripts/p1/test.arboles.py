from arboles.arboles import Arboles

arbol = Arboles()

datos_nuevo_arbol = {
    'especie': 'Pino Radiata',
    'diametro_cm': 45.5,
    'altura_m': 22.3,
    'volumen_m3': 1.8,
    'calidad_madera': 'Alta',
    'geom': 'POINT(5 5)' #parcela(norte)
}

print("Insertando")
resultado = arbol.insert(datos_nuevo_arbol)
print(resultado)