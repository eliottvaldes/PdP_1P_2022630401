"""
INTEGRANTES: 
- Díaz Jiménez Jorge Arif
- Delgado Acosta Luis Bernardo
- Valdés Luis Eliot Fabián
"""

"""
OBJETIVO:
Diseña y escribe un programa que, empleando Orientación a Objetos, determine
cuál es el par más cercano de puntos en 3D. Los puntos tendrán la estructura
P(x, y, z)
Ejemplos
P1=(2,3,4)
P2=(-2,3,9)
P3=(0.5,0.3,0.9)
• Preferentemente emplea la distancia Euclidiana.
• Deberás probar con al menos 20 puntos los cuales podrán generarse de manera aleatoria,
"""
# random para generar números aleatorios, 
import random

# math para realizar cálculos matemáticos 
import math

# combinations de itertools para generar combinaciones de puntos.
from itertools import combinations

# Definir una clase para implementar un punto en 3D
class Point3D:
    # definimos el constructor que inicia las coordenadas del punto
    def __init__(self, x, y, z):
        """
        Inicializa un punto en 3D con las coordenadas (x, y, z).
        """
        self.x = x
        self.y = y
        self.z = z

    # definimos el método para calcular la distancia entre dos puntos. usamos distancia euclidiana
    def distance_to(self, other_point):
        """
        Calcula y devuelve la distancia Euclidiana a otro punto.
        """
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2 + (self.z - other_point.z) ** 2)

    # definimos el método para imprimir el punto como una cadena de texto
    def __str__(self):
        """
        Convierte el punto a una cadena para facilitar la impresión.
        """
        return f"({self.x}, {self.y}, {self.z})"

# Función para encontrar el par de puntos más cercano
def closest_pair(points):
    """
    Encuentra y devuelve el par de puntos más cercano y su distancia.
    """
    # Inicializar la distancia mínima con infinito
    min_distance = float('inf')
    # Inicializar el par de puntos más cercano con None
    closest_pair = None

    # Iterar sobre todas las combinaciones de puntos
    for p1, p2 in combinations(points, 2):
        # obtenemos la distancia entre los puntos
        distance = p1.distance_to(p2)
        # verificar si la distancia es menor a la distancia mínima
        if distance < min_distance:
            min_distance = distance
            # si la distancia es menor, actualizamos el par de puntos más cercano
            closest_pair = (p1, p2)
    # retornamos el par de puntos más cercano y su distancia
    return closest_pair, min_distance



# PROBANDO IMPLEMENTACIÓN
# Generar 20 puntos aleatorios
points = [Point3D(random.random(), random.random(), random.random()) for _ in range(20)]

# Mostrar los puntos generados
print("==========================================================")
print(f'Puntos generados: { ", ".join(str(p) for p in points) }')
print("\n==========================================================")

# Encontrar el par de puntos más cercano
pair, distance = closest_pair(points)

print(f"\nEl par de puntos mas cercano es:\nPunto A: {pair[0]} \nPunto B: {pair[1]}. ")
print(f"La distancia entre ellos es: {distance}.\n")
