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
corriente = [0.84, 0.76, 0.7, 0.66, 0.58, 0.54, 0.5, 0.46, 0.42, 0.4, 0.36, 0.34, 0.31, 0.28, 0.26, 0.24,
             0.23, 0.21, 0.2, 0.19, 0.16, 0.16, 0.15, 0.14, 0.13, 0.12, 0.12, 0.11, 0.1, 0.1, 0.09, 0.09,
             0.08, 0.08, 0.08, 0.08, 0.07, 0.07, 0.07, 0.07, 0.07, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.05,
             0.05, 0.05, 0.05, 0.05, 0.05]

carga = [89288.6, 156490.02, 225571.2, 323788.66, 340706.5, 385350.8, 437044.2, 470409.94, 511764.66, 547010.16,
         578026.2, 606222.6, 632069.3, 656976.12, 676243.66, 695511.2, 714308.8, 731696.58, 746734.66, 759423.04,
         770701.6, 782920.04, 793728.66, 802657.52, 811586.38, 820045.3, 827564.34, 831793.8, 841662.54, 846361.94,
         852001.22, 857640.5, 861869.96, 865629.48, 869389.0, 873148.52, 876438.1, 879257.74, 881607.44, 883957.14,
         885836.9, 887716.66, 889126.48, 890536.3, 891476.18, 892416.06, 892886.0, 893355.94, 893825.88, 894295.82,
         894295.82, 894295.82, 894765.76]


arr_tiempo = np.array(tiempo)
arr_voltaje = np.array(voltaje)
arr_corriente = np.array(corriente)
arr_carga = np.array(carga)/1000000

# Función exponencial
def exponential_func(t, Qmax, RC):
    return Qmax * (1 - np.exp(-t / RC))


params, covariance = curve_fit(exponential_func, arr_tiempo, arr_carga)


#parámetros ajustados
Qmax_fit, RC_fit = params

# Coeficiente de correlación
residuals = arr_carga - exponential_func(arr_tiempo, Qmax_fit, RC_fit)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((arr_carga - np.mean(arr_carga))**2)
r_squared = 1 - (ss_res / ss_tot)

print(f"R cuadrado: {r_squared:.2f}")


# Gráfico
plt.scatter(arr_tiempo, arr_carga, label='Datos')
plt.plot(arr_tiempo, exponential_func(arr_tiempo, Qmax_fit, RC_fit), color='red', label='Regresión Exponencial')
plt.xlabel('Tiempo [s]')
plt.ylabel('Carga [MC]')
plt.legend()
plt.show()

# Imprimir la ecuación de la regresión
print("\nEcuación de la regresión exponencial:")
print("Q(t) =", (Qmax_fit*1000000), " * (1 - exp(-t /", RC_fit, "))")
print("\nRedondeado se obtiene:")
print(f"Q(t) = {(Qmax_fit*1000000):.2f} * (1 - exp(-t /{RC_fit:.2f}))")

# capacitancia en microfaradios
capacitancia_microfaradios = 4700
print(f"\ncapacitancia conocida en microfaradios: {capacitancia_microfaradios}")
# capacitancia a faradios
capacitancia_faradios = capacitancia_microfaradios * 1e-6

# valor de la resistencia en ohmios
resistencia_ohmios = RC_fit / capacitancia_faradios

# valor de la resistencia en kilo-Ohmios (kΩ)
resistencia_kilohmios = resistencia_ohmios / 1000

# redondeado en kΩ
resistencia_kilohmios_redondeada = round(resistencia_kilohmios)

# valor de la resistencia redondeada en kΩ
print("Valor de la resistencia (R):", resistencia_kilohmios_redondeada, "kΩ")


