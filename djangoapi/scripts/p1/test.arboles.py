from arboles.arboles import Arboles

arbol = Arboles()

datos_nuevo_arbol = {
    'especie': 'Pino Radiata',
    'diametro_cm': 45.5,
    'altura_m': 22.3,
    'volumen_m3': 1.8,
    'calidad_madera': 'Alta',
    'geom': 'POINT(5 5)' # ¡Cae dentro de la Parcela Norte!
}

print("--- INTENTANDO INSERTAR ARBOL ---")
resultado = arbol.insert(datos_nuevo_arbol)
print(resultado)