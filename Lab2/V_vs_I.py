import numpy as np
import matplotlib.pyplot as plt

def regression_lineal(x, y):
    #regresión lineal
    coeficientes = np.polyfit(x, y, 1)
    pendiente, interseccion = coeficientes

    # coeficiente de correlación
    correlacion = np.corrcoef(x, y)[0, 1]

    return pendiente, interseccion, correlacion

def grafico_dispersion_regresion(x, y, pendiente, interseccion):
    # gráfico
    plt.scatter(x, y, label='Datos')

    #línea de regresión
    regresion_y = pendiente * x + interseccion
    plt.plot(x, regresion_y, color='red', label='Regresión lineal')


    plt.xlabel('I [Amps]')
    plt.ylabel('V [volts]')
    plt.title('Gráfico de Voltaje vs Corriente')
    plt.legend()

    plt.show()

# Datos 

V = [1, 2, 4, 6, 8, 10, 12, 14]
I = [0.011, 0.021, 0.042, 0.063, 0.084, 0.105, 0.125, 0.146]


arr_V = np.array(V)
arr_I = np.array(I)

# regresión lineal 
pendiente, interseccion, correlacion = regression_lineal(arr_I, arr_V)

# Gráfico de dispersión con la regresión lineal
grafico_dispersion_regresion(arr_I, arr_V, pendiente, interseccion)

# ecuación de la recta
print(f'Ecuación de la recta: y = {pendiente:.3f}x + {interseccion:.3f}')
print(f'Coeficiente de correlación: {correlacion:.3f}')
print(f'Ecuación sin intersección: y = {pendiente:.3f}x')
print(f'Ecuación correspondiente a la ley de ohm: V = {pendiente:.3f} I => V=RI')
print(f'R = {pendiente:.3f} Ohms.')
