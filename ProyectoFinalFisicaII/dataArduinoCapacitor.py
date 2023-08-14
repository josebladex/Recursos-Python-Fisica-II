import numpy as np
import matplotlib.pyplot as plt
import math

from scipy.optimize import curve_fit
import serial

puerto = 'COM4'
baud_rate = 9600

try:
    with serial.Serial(puerto, baud_rate) as ser:
        data = ""  # Variable para almacenar los datos en formato string

        try:
            while True:
                linea = ser.readline().decode('utf-8').strip()
                print("Dato recibido:", linea)

                if linea.startswith('{') and linea.endswith('}'):
                    # Agregar la línea al final de la cadena de datos
                    data += linea + ','

                    # Lanzar una excepción KeyboardInterrupt para simular Ctrl + C
                    raise KeyboardInterrupt
                    
        except KeyboardInterrupt:
            pass  # Capturar la excepción y continuar con el flujo

except serial.SerialException as e:
    print("Error al abrir el puerto serie:", e)

# Eliminar la última coma de la cadena y agregar llaves para formar el JSON final
data = "" + data.rstrip(',') + ""
data = data[1:-1]


# Bloque de datos en una sola línea
data_str = data

# Dividir los datos en una lista de pares variable:valor
data_pairs = data_str.split(',')

# Inicializar arrays para almacenar los valores
tiempo= []
voltaje= []

# Iterar sobre los pares variable:valor y almacenar en los arrays correspondientes
for pair in data_pairs:
    variable, valor = pair.split(':')
    if variable == 'tiempo':
        tiempo.append(float(valor))
    elif variable == 'voltaje':
        voltaje.append(float(valor))

# Imprimir los arrays resultantes

print("Longitud de Tiempo:", len(tiempo))
print("Longitud de Voltaje:", len(voltaje))

# Convertir las listas a arrays de NumPy
arr_tiempo = np.array(tiempo)
arr_voltaje = np.array(voltaje)

# Función exponencial
def exponential_func(t, Vmax, RC):
    return Vmax * (1 - np.exp(-t / RC))


params, covariance = curve_fit(exponential_func, arr_tiempo, arr_voltaje)


# Obtener los parámetros ajustados
Vmax_fit, RC_fit = params

# Coeficiente de correlación (R cuadrado)
residuals = arr_voltaje - exponential_func(arr_tiempo, Vmax_fit, RC_fit)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((arr_voltaje - np.mean(arr_voltaje))**2)
r_squared = 1 - (ss_res / ss_tot)

print(f"R cuadrado: {r_squared:.2f}")


# Valor de la línea horizontal previamente calculada
horizontal_line = (1 - 1/np.e) * Vmax_fit

# Calcular punto de intersección
intersection_point = (RC_fit * np.log(Vmax_fit / (Vmax_fit - horizontal_line)), horizontal_line)

# Crear el gráfico
plt.figure(figsize=(8, 6))

# Agregar la línea horizontal y la línea vertical
plt.axhline(y=horizontal_line, color='green', linestyle='--', label='(1-1/e)Vmax')
plt.axvline(x=intersection_point[0], color='blue', linestyle='--', label='RC')

# Gráfico de los datos originales y la curva ajustada
plt.scatter(arr_tiempo, arr_voltaje, label='Datos')
plt.plot(arr_tiempo, exponential_func(arr_tiempo, Vmax_fit, RC_fit), color='red', label='Regresión Exponencial')

# Etiquetas y leyendas
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [V]')
plt.title('Voltaje Vs Tiempo del capacitor en carga')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()

# Imprimir la ecuación de la regresión
print("\nEcuación de la regresión exponencial:")
print("V(t) =", (Vmax_fit), " * (1 - exp(-t /", RC_fit, "))")
print("\nRedondeado se obtiene:")
print(f"V(t) = {(Vmax_fit):.2f} * (1 - exp(-t /{RC_fit:.2f}))")

# valor de la resistencia conocida en ohmios (Ω)
resistencia_ohmios = 10000

capacitancia =  RC_fit  / resistencia_ohmios * 1e6
   

print(f"Capacitancia: {capacitancia:.2f} µF")
