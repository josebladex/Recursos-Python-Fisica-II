array = [
  [2.0, 2.6, 2.9, 3.5, 4.1, 4.6, 5.2, 5.8, 6.4, 7.0, 7.5, 7.9, 8.4, 8.2, 9.4],
  [1.4, 2.0, 2.4, 3.1, 3.7, 4.4, 5.1, 5.8, 6.5, 7.1, 7.8, 8.4, 9.0, 9.2, 9.5],
  [1.3, 1.5, 1.8, 2.6, 3.3, 4.2, 5.0, 5.8, 6.6, 7.3, 8.2, 9.1, 9.7, 9.8, 9.8],
  [0.0, 0.0, 0.0, 2.0, 3.0, 4.0, 4.9, 5.8, 6.6, 7.5, 8.6, 9.7, 10.0, 10.0, 10.0],
  [0.0, 0.0, 0.0, 1.6, 2.9, 3.9, 4.9, 5.8, 6.6, 7.5, 8.7, 9.9, 10.0, 10.0, 10.0],
  [0.0, 0.0, 0.0, 2.0, 3.0, 4.0, 4.9, 5.8, 6.6, 7.5, 8.6, 9.7, 10.0, 10.0, 10.0],
  [1.3, 1.4, 1.8, 2.6, 3.4, 4.1, 5.0, 5.8, 6.6, 7.3, 8.2, 9.0, 9.6, 9.8, 9.8],
  [1.3, 2.0, 2.5, 3.2, 3.8, 4.5, 5.1, 5.8, 6.5, 7.1, 7.8, 8.4, 8.9, 9.2, 9.4],
  [1.9, 2.5, 3.0, 3.6, 4.1, 4.7, 5.2, 5.8, 6.4, 6.9, 7.5, 8.0, 8.4, 8.8, 9.6]
]

# superposición del potencial en cada punto
def calcular_superposicion(array):
    rows = len(array)
    cols = len(array[0])

    superposicion_array = [[0.0 for _ in range(cols)] for _ in range(rows)]


    for i in range(rows):
        for j in range(cols):
            superposicion_array[i][j] = array[i][j] + 10.0  # Sumamos 10V (voltaje del circuito)

    return superposicion_array


superposicion_result = calcular_superposicion(array)

for row in superposicion_result:
    print(row)

import numpy as np
import matplotlib.pyplot as plt

#campo eléctrico en cada punto
def calcular_campo_electrico(superposicion_array):
 
    rows, cols = len(superposicion_array), len(superposicion_array[0])

    # derivadas parciales 
    dy, dx = np.gradient(superposicion_array)

    # campo eléctrico como el gradiente negativo
    campo_electrico_x = -dx
    campo_electrico_y = -dy

    return campo_electrico_x, campo_electrico_y

# campo eléctrico a partir del array de la superposición
campo_electrico_x, campo_electrico_y = calcular_campo_electrico(superposicion_result)

# Creamos una malla de coordenadas 
x = np.arange(0, len(superposicion_result[0]), 1)
y = np.arange(0, len(superposicion_result), 1)
X, Y = np.meshgrid(x, y)

# Graficamos las líneas de campo eléctrico
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, campo_electrico_x, campo_electrico_y, scale=30, pivot="middle", color='b')
plt.xlabel('Posición en X [Centimetros]')
plt.ylabel('Posición en Y [Centimetros]')
plt.title("Líneas de Campo Eléctrico")
plt.show()