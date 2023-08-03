import numpy as np
import matplotlib.pyplot as plt

# Definición del array que contiene el mapa de potencial
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

# Convertir el array a un array NumPy
potential_map = np.array(array)

# Crear una malla de coordenadas para la superficie
x, y = np.meshgrid(np.arange(potential_map.shape[1]), np.arange(potential_map.shape[0]))

# Graficar la superficie equipotencial
plt.contour(x, y, potential_map, 50, cmap='viridis')  # Puedes ajustar el número de curvas (50 en este ejemplo)
plt.colorbar(label='Diferencia de Potencial [Volts]')  # Agregar la barra de color y etiquetarla
plt.xlabel('Posición en X [Centimetros]')
plt.ylabel('Posición en Y [Centimetros]')
plt.title('Superficies Equipotenciales')
plt.grid(True)
plt.show()
