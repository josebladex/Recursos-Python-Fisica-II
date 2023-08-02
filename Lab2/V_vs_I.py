import numpy as np
import matplotlib.pyplot as plt

def regression_lineal(x, y):
    # Ajustar una regresión lineal a los datos usando la función polyfit de numpy
    coeficientes = np.polyfit(x, y, 1)
    pendiente, interseccion = coeficientes

    # Calcular el coeficiente de correlación
    correlacion = np.corrcoef(x, y)[0, 1]

    return pendiente, interseccion, correlacion

def grafico_dispersion_regresion(x, y, pendiente, interseccion):
    # Crear el gráfico de dispersión
    plt.scatter(x, y, label='Datos')

    # Añadir la línea de regresión
    regresion_y = pendiente * x + interseccion
    plt.plot(x, regresion_y, color='red', label='Regresión lineal')

    # Personalizar el gráfico
    plt.xlabel('I [Amps]')
    plt.ylabel('V [volts]')
    plt.title('Gráfico de Voltaje vs Corriente')
    plt.legend()

    # Mostrar el gráfico
    plt.show()

# Datos de ejemplo (sustituye estos valores por tu propia matriz de datos)

# Valores para corriente vs inverso de resistencia y Corriente vs Resistencia

I = [1, 2, 4, 6, 8, 10, 12, 14]
V = [0.011, 0.021, 0.042, 0.063, 0.084, 0.105, 0.125, 0.146]

# Crear los np.array
arr_V = np.array(V)
arr_I = np.array(I)

# Encontrar la regresión lineal para corriente vs inverso de resistencia
pendiente, interseccion, correlacion = regression_lineal(arr_I, arr_V)

# Crear el gráfico de dispersión con la regresión lineal
grafico_dispersion_regresion(arr_I, arr_V, pendiente, interseccion)

# Imprimir la ecuación de la recta y otra información
print(f'Ecuación de la recta: y = {pendiente:.3f}x + {interseccion:.3f}')
print(f'Coeficiente de correlación: {correlacion:.3f}')
print(f'Ecuación sin intersección: y = {pendiente:.3f}x')
print(f'Ecuación correspondiente a la ley de ohm: V = {pendiente:.3f} I => V=RI')
print(f'R = {pendiente:.3f} Ohms.')
