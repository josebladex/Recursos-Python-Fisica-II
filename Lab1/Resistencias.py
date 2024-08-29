import pandas as pd

def calcular_error(valor_teorico, tolerancia_teorica, valor_experimental, tolerancia_experimental):
    # mínimo y máximo de la resistencia teórica con su tolerancia
    min_teorico = valor_teorico - tolerancia_teorica
    max_teorico = valor_teorico + tolerancia_teorica

    # mínimo y máximo de la resistencia experimental con su tolerancia
    min_experimental = valor_experimental - tolerancia_experimental
    max_experimental = valor_experimental + tolerancia_experimental

    #porcentaje de error para mínimo y máximo
    error_min = abs((min_teorico - min_experimental) / valor_teorico) * 100
    error_max = abs((max_teorico - max_experimental) / valor_teorico) * 100

    # tupla con los errores mínimo y máximo
    return error_min, error_max

# Datos
datos = [
    (300, 15, 293.8, 14.69),
    (150, 7.5, 148.4, 7.42),
    (1000000, 50000, 1100000, 55000),
    (51, 2.55, 51, 2.55),
    (570, 28.5, 481.9, 24.095),
    (18000, 900, 18180, 909),
    (390, 19.5, 383.1, 19.155),
    (62000, 3100, 59550, 2977.5),
    (100, 5, 99.3, 4.965),
    (5600, 280, 5580, 279),
    (200, 10, 200.5, 10.025)
]

resultados = []

# errores de medición para cada par de resistencias
for valor_teorico, tolerancia_teorica, valor_experimental, tolerancia_experimental in datos:
    error_min, error_max = calcular_error(valor_teorico, tolerancia_teorica, valor_experimental, tolerancia_experimental)
    resultados.append([valor_teorico, tolerancia_teorica, valor_experimental, tolerancia_experimental, error_min, error_max])

# DataFrame
columnas = ['Valor Teórico (Ohms)', 'Tolerancia Teórica (Ohms)', 'Valor Experimental (Ohms)', 'Tolerancia Experimental (Ohms)', 'Error Mínimo (%)', 'Error Máximo (%)']
df = pd.DataFrame(resultados, columns=columnas)

# Exportar DataFrame a Excel
nombre_archivo_excel = 'resultados_resistencias.xlsx'
df.to_excel(nombre_archivo_excel, index=False, engine='openpyxl')

print(f"Los resultados se han exportado a '{nombre_archivo_excel}' con éxito.")
