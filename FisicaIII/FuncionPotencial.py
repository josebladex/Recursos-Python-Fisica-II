

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x_distancia = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y_Intensidad = np.array([0.20, 0.30, 0.30, 0.45, 0.45, 0.63, 1.00, 1.90, 4.10, 11.00])

def regresion_potencial(x, a, b):
    return a * np.power(x, b)   # y=a(x^b)

# Parámetros de la regresión


params, covariance = curve_fit(regresion_potencial, x_distancia, y_Intensidad, maxfev=10000, p0=[1, 1], bounds=([0, 0], [np.inf, np.inf]))

a, b = params  # Parámetros de la regresión

print(f"Parámetro a: {a}")
print(f"Parámetro b: {b}")

# Calcular predicciones
y_pred = regresion_potencial(x_distancia, a, b)

# Calcular la media de y
y_mean = np.mean(y_Intensidad)

# Calcular el R cuadrado
SS_tot = np.sum((y_Intensidad - y_mean) ** 2)  # Suma de cuadrados total
SS_res = np.sum((y_Intensidad - y_pred) ** 2)  # Suma de cuadrados de la regresión
R_squared = 1 - (SS_res / SS_tot)

print(f"Coeficiente de correlación R^2: {R_squared}")


plt.figure(figsize=(8, 6))

# Gráfico de dispersión de puntos
plt.scatter(x_distancia, y_Intensidad, label='Datos', color='b')

# Curva de regresión potencial
x_range = np.linspace(min(x_distancia), max(x_distancia), 100)
plt.plot(x_range, regresion_potencial(x_range, a, b), label='Regresión Potencial', color='r')

# Etiquetas de ejes y título
plt.xlabel('Distancia')
plt.ylabel('Intensidad')
plt.title('Regresión Potencial de Intensidad vs. Distancia')

# Muestra la leyenda
plt.legend()

# Muestra el gráfico
plt.grid(True)
plt.show()

