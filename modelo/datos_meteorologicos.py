# modelo/datos_meteorologicos.py
import math
from collections import Counter

class DatosMeteorologicos:
    DIRECCIONES_VIENTO = {
        "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5, "E": 90, "ESE": 112.5,
        "SE": 135, "SSE": 157.5, "S": 180, "SSW": 202.5, "SW": 225,
        "WSW": 247.5, "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
    }

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo

    def procesar_datos(self) -> tuple[float, float, float, float, str]:
        temperaturas, humedades, presiones, velocidades, direcciones = [], [], [], [], []

        with open(self.nombre_archivo, "r") as archivo:
            for linea in archivo:
                datos = linea.split()
                temperatura = float(datos[7])
                humedad = float(datos[9])
                presion = float(datos[11])
                velocidad_viento = float(datos[13].split(',')[0])
                direccion_viento = datos[13].split(',')[1]

                temperaturas.append(temperatura)
                humedades.append(humedad)
                presiones.append(presion)
                velocidades.append(velocidad_viento)
                direcciones.append(direccion_viento)

        temp_promedio = sum(temperaturas) / len(temperaturas)
        humedad_promedio = sum(humedades) / len(humedades)
        presion_promedio = sum(presiones) / len(presiones)
        velocidad_promedio = sum(velocidades) / len(velocidades)
        direccion_predominante = self.calcular_direccion_predominante(direcciones)

        return temp_promedio, humedad_promedio, presion_promedio, velocidad_promedio, direccion_predominante

    def calcular_direccion_predominante(self, direcciones):
        direcciones_grados = [self.DIRECCIONES_VIENTO[dir] for dir in direcciones]
        suma_sen = sum(math.sin(math.radians(grados)) for grados in direcciones_grados)
        suma_cos = sum(math.cos(math.radians(grados)) for grados in direcciones_grados)
        angulo_promedio = math.degrees(math.atan2(suma_sen, suma_cos))
        if angulo_promedio < 0:
            angulo_promedio += 360

        direccion_predominante = min(self.DIRECCIONES_VIENTO, key=lambda d: abs(self.DIRECCIONES_VIENTO[d] - angulo_promedio))
        return direccion_predominante
