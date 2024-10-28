from modelo.datos_meteorologicos import DatosMeteorologicos

def main():
    archivo_datos = "resources/datos.txt"
    datos_meteorologicos = DatosMeteorologicos(archivo_datos)
    temp_promedio, humedad_promedio, presion_promedio, velocidad_promedio, direccion_predominante = datos_meteorologicos.procesar_datos()
    
    print("Estadísticas Meteorológicas:")
    print(f"Temperatura promedio: {temp_promedio:.2f}°C")
    print(f"Humedad promedio: {humedad_promedio:.2f}%")
    print(f"Presión promedio: {presion_promedio:.2f} hPa")
    print(f"Velocidad promedio del viento: {velocidad_promedio:.2f} km/h")
    print(f"Dirección predominante del viento: {direccion_predominante}")

if __name__ == "__main__":
    main()
