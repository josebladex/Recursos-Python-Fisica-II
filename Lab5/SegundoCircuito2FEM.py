from sympy import symbols, Eq, solve, Abs

def resolver_sistema(equations, I1, I2, I3, R1, R2, R3, R4, R5):
    # Resolver el sistema de ecuaciones
    sol = solve(equations, (I1, I2, I3))

    return sol

# Definir las corrientes como Incógnitas Algebraicas
I1, I2, I3 = symbols('I1 I2 I3')
# Definir las constantes (resistencias en Ohms)
R1 = 100
R2 = 200
R3 = 51
R4 = 300 
R5 = 150
# definir los voltajes del circuito
v1 = 20
v2 = 15

# Ingresar las ecuaciones manualmente como una lista de objetos Eq
# Por ejemplo, si las ecuaciones son R1*I1 + R3*I3 = -v  => escribimos Eq(R1*I1 + R3*I3, -v)
equations = [
    Eq(v1 -R1*I1 -R2*I1 -R3*I2, 0),   # Ley de Kirchoff de los voltajes en una malla cerrada
    Eq(-R4*I3 -R5*I3 + R3*I2 - v2, 0),
    Eq(I1 - I2 - I3, 0),    # Ley de Kirchoff de las corrientes en un nodo   
]

# Llamar a la función y obtener las soluciones
soluciones = resolver_sistema(equations, I1, I2, I3, R1, R2, R3, R4, R5)

Datos_teoricos = [Abs(soluciones[I1]), Abs(soluciones[I2]), Abs(soluciones[I3])]

# Mostrar las soluciones con cuatro decimales
print("\nDatos teóricos:")
for i, dato in enumerate(Datos_teoricos):
    print(f"Corriente {i+1} = {dato.evalf():.6f}")


# Definir un array con los valores experimentales
Datos_Experimentales = [0.055, 0.079, 0.024]

print("\nDatos Experimentales:")
for i, dato in enumerate(Datos_Experimentales):
    print(f"Corriente {i+1} = {dato}")



# Calcular el error porcentual entre los datos experimentales y los datos teóricos
errores_porcentuales = []
for i in range(len(Datos_Experimentales)):
    error_porcentual = abs(Datos_Experimentales[i] - Datos_teoricos[i].evalf()) / Datos_teoricos[i].evalf() * 100
    errores_porcentuales.append(error_porcentual)

# Mostrar los errores porcentuales
print("\nErrores porcentuales:")
for i, error in enumerate(errores_porcentuales):
    print(f"Error porcentual en Corriente {i+1} = {error:.2f}%")
