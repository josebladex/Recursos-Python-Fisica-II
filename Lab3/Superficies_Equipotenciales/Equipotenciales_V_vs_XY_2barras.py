import numpy as np
import matplotlib.pyplot as plt

# Definición del array de datos
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
