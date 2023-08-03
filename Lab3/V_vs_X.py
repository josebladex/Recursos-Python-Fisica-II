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
    plt.xlabel('X [centimetros]')
    plt.ylabel('V [volts]')
    plt.title('Gráfico de Voltaje vs Distancia')
    plt.legend()

    # Mostrar el gráfico
    plt.show()


# Valores para Voltaje vs Distancia
distancia = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
voltaje = [1.6, 3.0, 4.0, 5.0, 5.8, 6.7, 7.6, 8.9, 10.0]

# Crear los np.array
arr_V = np.array(voltaje)
arr_D = np.array(distancia)

# Encontrar la regresión lineal para corriente vs inverso de resistencia
pendiente, interseccion, correlacion = regression_lineal(arr_D, arr_V)

# Crear el gráfico de dispersión con la regresión lineal
grafico_dispersion_regresion(arr_D, arr_V, pendiente, interseccion)

# Imprimir la ecuación de la recta y otra información
print(f'Ecuación de la recta: y = {pendiente:.3f}x + {interseccion:.3f}')
print(f'Coeficiente de correlación: {correlacion:.3f}')
print(f'Ecuación sin intersección: y = {pendiente:.3f}x')
print(f'Ecuación correspondiente a la definicion de campo electrico V = {pendiente:.3f}*d => V=-Ed')
print(f'E = {pendiente:.3f} v/cm.')
