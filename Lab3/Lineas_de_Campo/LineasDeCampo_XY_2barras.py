array = [
    [1.8, 2.8, 3.8, 4.8, 5.8, 6.8, 7.8, 8.8, 9.8],
    [1.8, 2.8, 3.8, 4.8, 5.8, 6.8, 7.8, 8.8, 9.8],
    [1.8, 2.8, 3.8, 4.8, 5.8, 6.8, 7.8, 8.8, 9.8],
    [1.8, 2.8, 3.8, 4.8, 5.8, 6.8, 7.8, 8.8, 9.8],
    [1.8, 2.8, 3.8, 4.8, 5.8, 6.8, 7.8, 8.8, 9.8],
    [1.8, 2.8, 3.8, 4.8, 5.8, 6.8, 7.8, 8.8, 9.8],
    [1.8, 2.8, 3.8, 4.8, 5.8, 6.8, 7.8, 8.8, 9.8],
    [1.8, 2.8, 3.8, 4.8, 5.8, 6.8, 7.8, 8.8, 9.8],
    [1.8, 2.8, 3.8, 4.8, 5.8, 6.8, 7.8, 8.8, 9.8]
]

# superposición del potencial en cada punto
def calcular_superposicion(array):
    rows = len(array)
    cols = len(array[0])


    superposicion_array = [[0.0 for _ in range(cols)] for _ in range(rows)]

    # superposición en cada punto
    for i in range(rows):
        for j in range(cols):
            superposicion_array[i][j] = array[i][j] + 10.0  # 10V (voltaje del circuito)

    return superposicion_array


superposicion_result = calcular_superposicion(array)


for row in superposicion_result:
    print(row)

import numpy as np
import matplotlib.pyplot as plt

# campo eléctrico en cada punto
def calcular_campo_electrico(superposicion_array):
 
    rows, cols = len(superposicion_array), len(superposicion_array[0])

    # derivadas parciales
    dy, dx = np.gradient(superposicion_array)

    # campo eléctrico como el gradiente negativo
    campo_electrico_x = -dx
    campo_electrico_y = -dy

    return campo_electrico_x, campo_electrico_y

# campo eléctrico a partir del array
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