import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit


# Datos 
tiempo = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200,
          210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380,
          390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530]
voltaje = [1.9, 3.33, 4.8, 6.89, 7.25, 8.2, 9.3, 10.01, 10.89, 11.64, 12.3, 12.9, 13.45, 13.98, 14.39,
           14.8, 15.2, 15.57, 15.89, 16.16, 16.4, 16.66, 16.89, 17.08, 17.27, 17.45, 17.61, 17.7, 17.91,
           18.01, 18.13, 18.25, 18.34, 18.42, 18.5, 18.58, 18.65, 18.71, 18.76, 18.81, 18.85, 18.89, 18.92,
           18.95, 18.97, 18.99, 19.0, 19.01, 19.02, 19.03, 19.03, 19.03, 19.04]



arr_tiempo = np.array(tiempo)
arr_voltaje = np.array(voltaje)

# Función exponencial
def exponential_func(t, Vmax, RC):
    return Vmax * (1 - np.exp(-t / RC))


params, covariance = curve_fit(exponential_func, arr_tiempo, arr_voltaje)


# parámetros ajustados
Vmax_fit, RC_fit = params

# Coeficiente de correlación 
residuals = arr_voltaje - exponential_func(arr_tiempo, Vmax_fit, RC_fit)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((arr_voltaje - np.mean(arr_voltaje))**2)
r_squared = 1 - (ss_res / ss_tot)

print(f"R cuadrado: {r_squared:.2f}")


# Gráfico 
plt.scatter(arr_tiempo, arr_voltaje, label='Datos')
plt.plot(arr_tiempo, exponential_func(arr_tiempo, Vmax_fit, RC_fit), color='red', label='Regresión Exponencial')
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [v]')
plt.legend()
plt.show()

# ecuación de la regresión
print("\nEcuación de la regresión exponencial:")
print("V(t) =", (Vmax_fit), " * (1 - exp(-t /", RC_fit, "))")
print("\nRedondeado se obtiene:")
print(f"V(t) = {(Vmax_fit):.2f} * (1 - exp(-t /{RC_fit:.2f}))")

# capacitancia en microfaradios
capacitancia_microfaradios = 4700
print(f"\ncapacitancia conocida en microfaradios: {capacitancia_microfaradios}")
#capacitancia a faradios
capacitancia_faradios = capacitancia_microfaradios * 1e-6

# resistencia en ohmios
resistencia_ohmios = RC_fit / capacitancia_faradios

# resistencia en kiloohmios (kΩ)
resistencia_kilohmios = resistencia_ohmios / 1000

# redondeado en kΩ
resistencia_kilohmios_redondeada = round(resistencia_kilohmios)

# resistencia redondeada en kΩ
print("Valor de la resistencia (R):", resistencia_kilohmios_redondeada, "kΩ")


