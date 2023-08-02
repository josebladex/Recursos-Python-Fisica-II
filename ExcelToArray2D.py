import numpy as np

# Crear el array multidimensional usando NumPy
data = """
2.8	2.8	3	3.5	4.1	4.8	5.6	6.3	7.2	8	9
2.3	2.4	2.5	3	3.7	4.5	5.4	6.3	7.2	8.2	9.1
1.8	1.7	1.8	2.4	3.4	4.4	5.3	6.3	7.2	8.1	9.1
0	0	0	1.8	3	4.2	5.2	6.2	7.1	8.1	9.2
0	0	0	1.5	2.8	4.1	5.2	6.2	7.2	8.2	9.2
0	0	0	1.9	3	4.2	5.3	6.2	7.2	8.2	9.2
1.8	1.7	1.8	2.6	3.5	4.5	5.4	6.3	7.3	8.2	9.1
2.3	2.4	2.7	3.2	4	4.7	5.5	6.5	7.3	8.2	9.1
2.8	2.9	3.2	3.7	4.2	5	5.7	6.5	7.4	8.2	9.1
"""

lines = data.strip().split("\n")
array_bidimensional = []
for line in lines:
    values = line.split()
    array_bidimensional.append([float(value.replace(",", ".")) for value in values])

# Convertir el array a formato string con corchetes y comas
array_string = "["
for row in array_bidimensional:
    row_string = "[" + ", ".join([str(elem) for elem in row]) + "]"
    array_string += row_string + ","
array_string = array_string.rstrip(",") + "]"

# Imprimir el resultado con el formato solicitado
print("array =", array_string)
