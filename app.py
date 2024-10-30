from modelo.datos_meteorologicos import DatosMeteorologicos

datos_meteorologicos = DatosMeteorologicos("assets/datos.txt")
print(datos_meteorologicos.procesar_datos())
