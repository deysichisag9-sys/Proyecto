from parcelas.parcelas import ParcelasOOP

# Inicializamos la clase
parcela = ParcelasOOP()

# 1. Definimos los datos a insertar
datos_nueva = {
    'nombre': 'Segunda Parcela Wilson',
    'propietario': 'Aserradero y deposito Wilson',
    'area_ha': 45.5,
    'tipo_bosque': 'Pino',
    'estado_legal': 'Propio',
    'perimetro': 950.0,
    # ¡Cambiamos los 2000 por 3000!
    'geom': 'POLYGON((3000 3000, 3010 3000, 3010 3010, 3000 3010, 3000 3000))' 
}

# 2. Ejecutamos el insert
resultado_insert = parcela.insert(datos_nueva)

# 3. Imprimimos el resultado en la consola
print(resultado_insert)



