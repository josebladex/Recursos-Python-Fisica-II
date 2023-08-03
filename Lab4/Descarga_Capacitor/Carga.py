import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit


# Datos proporcionados
tiempo = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 120.0, 130.0, 140.0, 150.0, 
          160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 
          300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 
          440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 
          580.0, 590.0, 600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 700.0, 710.0, 
          720.0, 730.0, 740.0, 750.0, 760.0, 770.0, 780.0, 790.0, 800.0, 810.0, 820.0, 830.0, 840.0, 850.0]     
voltaje = [16.81, 15.55, 14.38, 13.21, 12.19, 11.24, 10.38, 9.6, 8.82, 8.18, 7.54, 7.02, 6.53, 6.01, 5.28, 
           5.18, 4.72, 4.35, 4.02, 3.72, 3.45, 3.12, 2.93, 2.5, 2.48, 2.32, 2.16, 2.01, 1.85, 1.73, 1.6, 1.5, 
           1.34, 1.29, 1.2, 1.12, 1.04, 0.98, 0.91, 0.85, 0.8, 0.75, 0.7, 0.65, 0.63, 0.6, 0.57, 0.54, 0.51,
           0.48, 0.45, 0.42, 0.4, 0.38, 0.35, 0.34, 0.32, 0.3, 0.28, 0.27, 0.25, 0.24, 0.23, 0.21, 0.2, 0.19, 
           0.18, 0.17, 0.16, 0.16, 0.15, 0.14, 0.14, 0.14, 0.13, 0.13, 0.12, 0.12, 0.12, 0.11, 0.11, 0.1, 0.1, 
           0.1, 0.09]
corriente = [0.78, 0.72, 0.67, 0.62, 0.57, 0.52, 0.49, 0.44, 0.41, 0.39, 0.37, 0.33, 0.29, 0.27, 0.25, 0.23, 
             0.22, 0.2, 0.18, 0.17, 0.16, 0.14, 0.13, 0.12, 0.11, 0.1, 0.1, 0.09, 0.08, 0.08, 0.07, 0.07, 0.06,
               0.06, 0.06, 0.05, 0.05, 0.04, 0.04, 0.04, 0.04, 0.03, 0.03, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02,
                 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                   0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                     0.01, 0.01, 0.01, 0.01]
carga = [789969.14, 730756.7, 675773.72, 620790.74, 572856.86, 528212.56, 487797.72, 451142.4, 414487.08, 384410.92,
          354334.76, 329897.88, 306870.82, 282433.94, 248128.32, 243428.92, 221811.68, 204423.9, 188915.88, 174817.68,
            162129.3, 146621.28, 137692.42, 117485.0, 116545.12, 109026.08, 101507.04, 94457.94, 86938.9, 81299.62, 
            75190.4, 70491.0, 62971.96, 60622.26, 56392.8, 52633.28, 48873.76, 46054.12, 42764.54, 39944.9, 37595.2, 
            35245.5, 32895.8, 30546.1, 29606.22, 28196.4, 26786.58, 25376.76, 23966.94, 22557.12, 21147.3, 19737.48, 
            18797.6, 17857.72, 16447.9, 15977.96, 15038.08, 14098.2, 13158.32, 12688.38, 11748.5, 11278.56, 10808.62,
            9868.74, 9398.8, 8928.86, 8458.92, 7988.98, 7519.04, 7519.04, 7049.1, 6579.16, 6579.16, 6579.16, 6109.22, 
            6109.22, 5639.28, 5639.28, 5639.28, 5169.34, 5169.34, 4699.4, 4699.4, 4699.4, 4229.46]

# Convertir las listas a arrays de NumPy
arr_tiempo = np.array(tiempo)
arr_voltaje = np.array(voltaje)
arr_corriente = np.array(corriente)
arr_carga = np.array(carga)/1000000

# Función exponencial
def exponential_func(x, a, b):
    return a * (np.exp(b*x))

initial_guess = (1.0, -0.01)  # You can adjust these initial values based on your data
params, covariance = curve_fit(exponential_func, arr_tiempo, arr_carga, p0=initial_guess)


# Obtener los parámetros ajustados
a_fit, b_fit = params

# Coeficiente de correlación (R cuadrado)
residuals = arr_carga - exponential_func(arr_tiempo, a_fit, b_fit)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((arr_carga - np.mean(arr_carga))**2)
r_squared = 1 - (ss_res / ss_tot)

print(f"R cuadrado: {r_squared:.2f}")


# Gráfico de los datos originales y la curva ajustada
plt.scatter(arr_tiempo, arr_carga, label='Datos')
plt.plot(arr_tiempo, exponential_func(arr_tiempo, a_fit, b_fit), color='red', label='Regresión Exponencial')
plt.xlabel('Tiempo [s]')
plt.ylabel('Carga [MC]')
plt.legend()
plt.show()

# Imprimir la ecuación de la regresión
print("\nEcuación de la regresión exponencial:")
print("y=", (a_fit*1000000), " * (e^(", b_fit, "*x))")
print("\nRedondeado y ajustando a la ecuacion de Q en descarga se obtiene:")
print(f"Q(t) = {(a_fit*1000000):.2f} * (e^({b_fit:.2f}*t))")

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


