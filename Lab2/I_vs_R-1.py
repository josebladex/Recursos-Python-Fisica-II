import numpy as np
import matplotlib.pyplot as plt

def regression_lineal(x, y):
    # Ajustar una regresión lineal
    coeficientes = np.polyfit(x, y, 1)
    pendiente, interseccion = coeficientes

    # coeficiente de correlación
    correlacion = np.corrcoef(x, y)[0, 1]

    return pendiente, interseccion, correlacion

def grafico_dispersion_regresion(x, y, pendiente, interseccion):
    #gráfico de dispersión
    plt.scatter(x, y, label='Datos')

    # línea de regresión
    regresion_y = pendiente * x + interseccion
    plt.plot(x, regresion_y, color='red', label='Regresión lineal')


    plt.xlabel('1/R [Ohms^-1]')
    plt.ylabel('I [Amps]')
    plt.title('Gráfico de Corriente vs Resistencia Inversa')
    plt.legend()

    plt.show()


# corriente vs inverso de resistencia y Corriente vs Resistencia
R = [10, 20, 30, 40, 50, 60, 70, 80, 90, 97]
I = [0.547, 0.256, 0.169, 0.129, 0.102, 0.085, 0.073, 0.064, 0.057, 0.052]


arr_R = np.array(R)
arr_I = np.array(I)
arr_R_inv = 1 / arr_R

# regresión lineal para corriente vs inverso de resistencia
pendiente, interseccion, correlacion = regression_lineal(arr_R_inv, arr_I)

# gráfico de dispersión con la regresión lineal
grafico_dispersion_regresion(arr_R_inv, arr_I, pendiente, interseccion)

# ecuación de la recta
print(f'Ecuación de la recta: y = {pendiente:.3f}x + {interseccion:.3f}')
print(f'Coeficiente de correlación: {correlacion:.3f}')
print(f'Ecuación sin intersección: y = {pendiente:.3f}x')
print(f'Ecuación correspondiente a la ley de ohm: I = {pendiente:.3f}/R => I=V/R')
print(f'V = {pendiente:.3f}v.')
