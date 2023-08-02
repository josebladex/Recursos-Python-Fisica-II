array = [
  [2.8, 2.8, 3.0, 3.5, 4.1, 4.8, 5.6, 6.3, 7.2, 8.0, 9.0],
  [2.3, 2.4, 2.5, 3.0, 3.7, 4.5, 5.4, 6.3, 7.2, 8.2, 9.1],
  [1.8, 1.7, 1.8, 2.4, 3.4, 4.4, 5.3, 6.3, 7.2, 8.1, 9.1],
  [0.0, 0.0, 0.0, 1.8, 3.0, 4.2, 5.2, 6.2, 7.1, 8.1, 9.2],
  [0.0, 0.0, 0.0, 1.5, 2.8, 4.1, 5.2, 6.2, 7.2, 8.2, 9.2],
  [0.0, 0.0, 0.0, 1.9, 3.0, 4.2, 5.3, 6.2, 7.2, 8.2, 9.2],
  [1.8, 1.7, 1.8, 2.6, 3.5, 4.5, 5.4, 6.3, 7.3, 8.2, 9.1],
  [2.3, 2.4, 2.7, 3.2, 4.0, 4.7, 5.5, 6.5, 7.3, 8.2, 9.1],
  [2.8, 2.9, 3.2, 3.7, 4.2, 5.0, 5.7, 6.5, 7.4, 8.2, 9.1]
]


# Definimos una función para calcular la superposición del potencial en cada punto
def calcular_superposicion(array):
    rows = len(array)
    cols = len(array[0])

    # Creamos un nuevo array para almacenar los resultados de la superposición
    superposicion_array = [[0.0 for _ in range(cols)] for _ in range(rows)]

    # Calculamos la superposición en cada punto
    for i in range(rows):
        for j in range(cols):
            superposicion_array[i][j] = array[i][j] + 10.0  # Sumamos 10V (voltaje del circuito)

    return superposicion_array

# Calculamos la superposición y almacenamos el resultado en una nueva variable
superposicion_result = calcular_superposicion(array)

# Imprimimos el nuevo array resultante
for row in superposicion_result:
    print(row)

import numpy as np
import matplotlib.pyplot as plt

# Definimos una función para calcular el campo eléctrico en cada punto
def calcular_campo_electrico(superposicion_array):
    # Obtenemos las dimensiones del array
    rows, cols = len(superposicion_array), len(superposicion_array[0])

    # Calculamos las derivadas parciales utilizando np.gradient
    dy, dx = np.gradient(superposicion_array)

    # Calculamos el campo eléctrico como el gradiente negativo
    campo_electrico_x = -dx
    campo_electrico_y = -dy

    return campo_electrico_x, campo_electrico_y

# Calculamos el campo eléctrico a partir del array de la superposición
campo_electrico_x, campo_electrico_y = calcular_campo_electrico(superposicion_result)

# Creamos una malla de coordenadas para realizar la gráfica
x = np.arange(0, len(superposicion_result[0]), 1)
y = np.arange(0, len(superposicion_result), 1)
X, Y = np.meshgrid(x, y)

# Graficamos las líneas de campo eléctrico con quiver
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, campo_electrico_x, campo_electrico_y, scale=30, pivot="middle", color='b')
plt.xlabel("Coordenada x")
plt.ylabel("Coordenada y")
plt.title("Líneas de Campo Eléctrico")
plt.show()