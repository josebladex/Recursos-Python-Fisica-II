import numpy as np
import matplotlib.pyplot as plt

# Definición del array de datos
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


potential_map = np.array(array)

# Crear una malla de coordenadas para la superficie
x, y = np.meshgrid(np.arange(potential_map.shape[1]), np.arange(potential_map.shape[0]))

# Graficar la superficie equipotencial
plt.contour(x, y, potential_map, 50, cmap='viridis')  # Puedes ajustar el número de curvas (50 en este ejemplo)
plt.colorbar(label='Diferencia de Potencial [Volts]')  
plt.xlabel('Posición en X [Centimetros]')
plt.ylabel('Posición en Y [Centimetros]')
plt.title('Superficies Equipotenciales')
plt.grid(True)
plt.show()
