import numpy as np
import matplotlib.pyplot as plt

def regression_potencial(x, y):
    # Ajustar una regresión potencial a los datos usando la función polyfit de numpy
    coeficientes = np.polyfit(np.log(x), np.log(y), 1)
    a = coeficientes[1]
    b = coeficientes[0]

    # Calcular el coeficiente de correlación
    correlacion = np.corrcoef(np.log(x), np.log(y))[0, 1]

    # Ecuación de la regresión potencial
    # La ecuación es de la forma: y = c * x^b
    c = np.exp(a)

    return b, c, correlacion

def grafico_dispersion_regresion_potencial(x, y, b, c):
    # Crear el gráfico de dispersión
    plt.scatter(x, y, label='Datos')

    # Añadir la línea de regresión potencial
    x_vals = np.linspace(min(x), max(x), 100)
    regresion_y = c * x_vals**b
    plt.plot(x_vals, regresion_y, color='red', label='Regresión potencial')

    # Personalizar el gráfico
    plt.xlabel('R [Ohms]')
    plt.ylabel('I [Amps]')
    plt.title('Gráfico de Corriente vs Resistencia')
    plt.legend()

    # Mostrar el gráfico
    plt.show()

# Datos de ejemplo (sustituye estos valores por tu propia matriz de datos)
R = [10, 20, 30, 40, 50, 60, 70, 80, 90, 97]
I = [0.547, 0.256, 0.169, 0.129, 0.102, 0.085, 0.073, 0.064, 0.057, 0.052]

# Crear los np.array
arr_R = np.array(R)
arr_I = np.array(I)

# Realizar la regresión potencial
b, c, correlacion = regression_potencial(arr_R, arr_I)

# Imprimir la ecuación de la regresión potencial y el coeficiente de correlación
print(f'Ecuación de la regresión potencial: y = {c:.3f} * x^{b:.3f}')
print(f'Coeficiente de correlación: {correlacion:.3f}')
print(f'Ecuación correspondiente a la ley de ohm: I = {c:.3f} * R^{b:.0f} => I=V/R')
print(f'V = {c:.2f} volts.')

# Crear el gráfico de dispersión con la regresión potencial
grafico_dispersion_regresion_potencial(arr_R, arr_I, b, c)
