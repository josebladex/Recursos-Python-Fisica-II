import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



# Datos de tiempo (en segundos) y corriente
tiempo = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 120.0, 130.0, 140.0, 150.0, 160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0]     
corriente = [0.78, 0.72, 0.67, 0.62, 0.57, 0.52, 0.49, 0.44, 0.41, 0.39, 0.37, 0.33, 0.29, 0.27, 0.25, 0.23, 0.22, 0.2, 0.18, 0.17, 0.16, 0.14, 0.13, 0.12, 0.11, 0.1, 0.1, 0.09, 0.08, 0.08, 0.07, 0.07, 0.06, 0.06, 0.06, 0.05, 0.05, 0.04, 0.04, 0.04, 0.04, 0.03, 0.03, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]

arr_tiempo = np.array(tiempo)
arr_corriente = np.array(corriente)


# Función exponencial para la regresión
def funcion_exponencial(x, a, b):
    return a * np.exp(b * x) 

# Ajuste de la regresión exponencial
initial_guess = (1.0, -0.01)  # You can adjust these initial values based on your data
params, covariance = curve_fit(funcion_exponencial, arr_tiempo, arr_corriente, p0=initial_guess)

# Extraer los parámetros a y b de la ecuación exponencial
a_fit, b_fit = params

print("y =", a_fit, " * e^(", b_fit, "x)")

# Coeficiente de correlación (R cuadrado)
residuals = arr_corriente - funcion_exponencial(arr_tiempo, a_fit, b_fit)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((arr_corriente - np.mean(arr_corriente))**2)
r_squared = 1 - (ss_res / ss_tot)


# Imprimir la ecuación de la regresión :.2f
print("\nEcuación de la regresión exponencial:")
print("y =", a_fit, " * e^(", b_fit, "x)")
print("\nRedondeado se obtiene:")
print(f'y =" {a_fit:.2f}" * e^(" {b_fit:.2f} "x)')
print(f'Ecuación correspondiente a descarga del capacitor I =" {a_fit:.2f}, " * e^(" {b_fit:.2f} "t) => I = I°* e^((-1/RC)t)')
print(f'I =" {a_fit:.2f}" * e^(" {b_fit:.2f} "t) Amps')
# Imprimir el coeficiente de correlación (R cuadrado)
print("\nCoeficiente de correlación (R cuadrado):")
print("R^2 =", r_squared)

# Graficar los datos y la regresión exponencial
plt.scatter(tiempo, corriente, marker='o', color='blue', label='Descarga de condensador')
plt.plot(arr_tiempo, funcion_exponencial(arr_tiempo, a_fit, b_fit), color='red', label='Regresión Exponencial')
plt.xlabel('Tiempo [s]')
plt.ylabel('Corriente [A]')
plt.title('Gráfica de Dispersión: Corriente vs Tiempo')
plt.legend()
plt.grid(True)
plt.show()



# Valor conocido de la capacitancia en microfaradios
capacitancia_microfaradios = 4700
print(f"\ncapacitancia conocida en microfaradios: {capacitancia_microfaradios}")
# Convertir la capacitancia a faradios
capacitancia_faradios = capacitancia_microfaradios * 1e-6

# Calcular el valor de la resistencia en ohmios
resistencia_ohmios = 1 /(-1 *b_fit * capacitancia_faradios)

# Calcular el valor de la resistencia en kiloohmios (kΩ)
resistencia_kilohmios = resistencia_ohmios / 1000

# Valor redondeado en kΩ
resistencia_kilohmios_redondeada = round(resistencia_kilohmios)

# Imprimir el valor de la resistencia redondeada en kΩ
print("Valor de la resistencia (R):", resistencia_kilohmios_redondeada, "kΩ")


