# Capacitance Reader Project

## 📘 Overview

Welcome to the **Capacitance Reader Project**! This project combines an Arduino-based capacitance measurement system with a Python script for data analysis. The Arduino sketch captures the charging characteristics of a capacitor, while the Python script processes and visualizes the data to determine the capacitance value.

## 🚀 Project Components

### Arduino Code

The Arduino code is designed to:
- **Initialize**: Set up the pins for capacitor charging and discharging.
- **Discharge the Capacitor**: Ensure the capacitor is fully discharged before starting a new measurement.
- **Charge the Capacitor**: Measure the voltage across the capacitor as it charges and record the time.
- **Output Data**: Send data in JSON format for further analysis.

### Python Code

The Python script performs the following tasks:
- **Serial Communication**: Reads and collects data from the Arduino.
- **Data Processing**: Parses JSON data, extracts time and voltage values.
- **Curve Fitting**: Applies an exponential model to the data to determine the capacitance.
- **Plotting**: Visualizes the data and the fitted curve to understand the capacitor's charging behavior.

## 📈 Results

- **R-Squared Value**: Provides insight into the goodness of fit for the exponential model.
- **Capacitance Calculation**: Derived from the fitted curve parameters and a known resistance value.

## 🎥 Reference Video

For a deeper understanding of the principles involved in this project, check out this informative [YouTube video](https://www.youtube.com/watch?v=CbOFaja7_yc).

## 📜 License

This project is licensed under the MIT License.

## 📌 Repository

The code and detailed instructions are available in this repository. Please refer to the respective files for implementation details.

Thank you for exploring the Capacitance Reader Project!

---

# Proyecto Lector de Capacitancia

## 📘 Visión General

¡Bienvenido al **Proyecto Lector de Capacitancia**! Este proyecto combina un sistema de medición de capacitancia basado en Arduino con un script en Python para el análisis de datos. El sketch de Arduino captura las características de carga de un condensador, mientras que el script en Python procesa y visualiza los datos para determinar el valor de la capacitancia.

## 🚀 Componentes del Proyecto

### Código de Arduino

El código de Arduino está diseñado para:
- **Inicializar**: Configurar los pines para la carga y descarga del condensador.
- **Descargar el Condensador**: Asegurarse de que el condensador esté completamente descargado antes de comenzar una nueva medición.
- **Cargar el Condensador**: Medir el voltaje a través del condensador mientras se carga y registrar el tiempo.
- **Enviar Datos**: Enviar los datos en formato JSON para su análisis posterior.

### Código en Python

El script en Python realiza las siguientes tareas:
- **Comunicación Serial**: Lee y recoge datos del Arduino.
- **Procesamiento de Datos**: Analiza los datos JSON, extrae los valores de tiempo y voltaje.
- **Ajuste de Curva**: Aplica un modelo exponencial a los datos para determinar la capacitancia.
- **Graficado**: Visualiza los datos y la curva ajustada para comprender el comportamiento de carga del condensador.

## 📈 Resultados

- **Valor R-Cuadrado**: Proporciona información sobre la calidad del ajuste del modelo exponencial.
- **Cálculo de la Capacitancia**: Derivado de los parámetros del ajuste de la curva y un valor de resistencia conocido.

## 🎥 Video de Referencia

Para una comprensión más profunda de los principios involucrados en este proyecto, consulta este [video de YouTube](https://www.youtube.com/watch?v=CbOFaja7_yc).

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT.

## 📌 Repositorio

El código y las instrucciones detalladas están disponibles en este repositorio. Consulta los archivos respectivos para detalles de implementación.

¡Gracias por explorar el Proyecto Lector de Capacitancia!
