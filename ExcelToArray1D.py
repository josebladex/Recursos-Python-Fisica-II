import numpy as np

# Datos proporcionados
data = """
d	V
1	1,6
2	3
3	4
4	5
5	5.8
6	6.7
7	7.6
8	8.9
9	10
"""

# Dividir el texto en líneas y eliminar líneas vacías
lines = data.strip().split("\n")

# Inicializar las listas vacías para cada columna
distancia = []
voltaje = []

# Recorrer las líneas de datos y agregar valores a las listas correspondientes
for line in lines[1:]:
    values = line.split()
    distancia.append(float(values[0].replace(",", ".")))  # Reemplazar la coma por el punto decimal
    voltaje.append(float(values[1].replace(",", ".")))  # Reemplazar la coma por el punto decimal

# Convertir las listas en arrays de NumPy para facilitar su manipulación
arr_distancia = np.array(distancia)
arr_voltaje = np.array(voltaje)

# Imprimir los arrays resultantes
print("Distancia:", arr_distancia)
print("Voltaje:", arr_voltaje)

print("Longitud de arr_distancia:", len(arr_distancia))
print("Longitud de arr_voltaje:", len(arr_voltaje))


def print_array_with_format(arr, label):
    elements = ", ".join([str(elem) for elem in arr])
    print(label + " =", "[" + elements + "]")

# Imprimir los arrays resultantes con el formato solicitado
print_array_with_format(arr_distancia, "distancia")
print_array_with_format(arr_voltaje, "voltaje")
