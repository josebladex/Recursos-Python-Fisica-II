#/****************************************************************************************
# *                                Proyecto Final Fisica II                             *
# *              Universidad de Panamá - José Plata, Karen González, Joseph Chamarra    *
# **************************************************************************************/

import numpy as np  # Importa la librería NumPy para cálculos numéricos eficientes
import matplotlib.pyplot as plt  # Importa la librería Matplotlib para la creación de gráficos
import math  # Importa el módulo math para funciones matemáticas
from scipy.optimize import curve_fit  # Importa la función curve_fit de SciPy para ajuste de curvas
import serial  # Importa la librería Serial para la comunicación con puertos seriales

puerto = 'COM4'  # Define el nombre del puerto serial a 'COM4'
baud_rate = 9600  # Define la velocidad de transmisión en baudios

try:
    with serial.Serial(puerto, baud_rate) as ser:  # Intenta abrir el puerto serial
        data = ""  # Inicializa una cadena para almacenar datos en formato string
        try:
            while True:  # Bucle infinito
                linea = ser.readline().decode('utf-8').strip()  # Lee una línea del puerto y la decodifica
                if linea.startswith('{') and linea.endswith('}'):  # Si la línea empieza con '{' y termina con '}'
                    data += linea + ','  # Agrega la línea al final de la cadena de datos
                    raise KeyboardInterrupt  # Simula una interrupción de teclado para salir del bucle
        except KeyboardInterrupt:  # Captura una excepción KeyboardInterrupt
            pass  # Continúa con la ejecución del programa

except serial.SerialException as e:  # Captura una excepción si hay un error en el puerto serial
    print("Error al abrir el puerto serie:", e)

data = "" + data.rstrip(',') + ""  # Elimina la última coma de la cadena de datos y agrega llaves para formar JSON
data_str = data  # Almacena la cadena de datos en otra variable
data_pairs = data_str.split(',')  # Divide la cadena de datos en una lista de pares variable:valor
tiempo = []  # Inicializa una lista para almacenar los valores de tiempo
voltaje = []  # Inicializa una lista para almacenar los valores de voltaje

for pair in data_pairs:  # Itera sobre los pares variable:valor en la lista
    variable, valor = pair.split(':')  # Divide el par en variable y valor
    if variable == 'tiempo':  # Si la variable es 'tiempo'
        tiempo.append(float(valor))  # Convierte y agrega el valor a la lista de tiempo como flotante
    elif variable == 'voltaje':  # Si la variable es 'voltaje'
        voltaje.append(float(valor))  # Convierte y agrega el valor a la lista de voltaje como flotante

arr_tiempo = np.array(tiempo)  # Convierte la lista de tiempo en un array de NumPy
arr_voltaje = np.array(voltaje)  # Convierte la lista de voltaje en un array de NumPy

def exponential_func(t, Vmax, RC):  # Define una función exponencial con parámetros Vmax y RC
    return Vmax * (1 - np.exp(-t / RC))  # Retorna el valor de la función exponencial

params, covariance = curve_fit(exponential_func, arr_tiempo, arr_voltaje)  # Ajusta la curva exponencial a los datos
Vmax_fit, RC_fit = params  # Almacena los parámetros ajustados Vmax y RC
residuals = arr_voltaje - exponential_func(arr_tiempo, Vmax_fit, RC_fit)  # Calcula los residuos
ss_res = np.sum(residuals**2)  # Calcula la suma de los residuos al cuadrado
ss_tot = np.sum((arr_voltaje - np.mean(arr_voltaje))**2)  # Calcula la suma total al cuadrado
r_squared = 1 - (ss_res / ss_tot)  # Calcula el coeficiente de correlación R cuadrado

horizontal_line = (1 - 1/np.e) * Vmax_fit  # Calcula el valor de la línea horizontal
intersection_point = (RC_fit * np.log(Vmax_fit / (Vmax_fit - horizontal_line)), horizontal_line)  # Calcula el punto de intersección

plt.figure(figsize=(8, 6))  # Crea una figura para el gráfico con tamaño 8x6
plt.axhline(y=horizontal_line, color='green', linestyle='--', label='(1-1/e)Vmax')  # Agrega una línea horizontal al gráfico
plt.axvline(x=intersection_point[0], color='blue', linestyle='--', label='RC')  # Agrega una línea vertical al gráfico
plt.scatter(arr_tiempo, arr_voltaje, label='Datos')  # Agrega puntos para los datos originales
plt.plot(arr_tiempo, exponential_func(arr_tiempo, Vmax_fit, RC_fit), color='red', label='Regresión Exponencial')  # Agrega la curva ajustada
plt.xlabel('Tiempo [s]')  # Etiqueta del eje x
plt.ylabel('Voltaje [V]')  # Etiqueta del eje y
plt.title('Voltaje Vs Tiempo del capacitor en carga')  # Título del gráfico
plt.legend()  # Muestra las leyendas
plt.grid(True)  # Agrega una cuadrícula al gráfico
plt.show()  # Muestra el gráfico

print("\nEcuación de la regresión exponencial:")  # Imprime un mensaje
print("V(t) =", (Vmax_fit), " * (1 - exp(-t /", RC_fit, "))")  # Imprime la ecuación de la regresión
print("\nRedondeado se obtiene:")  # Imprime un mensaje
print(f"V(t) = {(Vmax_fit):.2f} * (1 - exp(-t /{RC_fit:.2f}))")  # Imprime la ecuación redondeada

resistencia_ohmios = 10000  # Define el valor de la resistencia en ohmios
capacitancia =  RC_fit  / resistencia_ohmios * 1e6  # Calcula la capacitancia en microfaradios
print(f"Capacitancia: {capacitancia:.2f} µF")  # Imprime el valor de la capacitancia
