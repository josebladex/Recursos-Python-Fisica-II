from sympy import symbols, Eq, solve

def resolver_sistema_ecuaciones():
    # Definir los símbolos para las variables desconocidas
    I_1, I_2, I_3, I_4, I_5 = symbols('I_1 I_2 I_3 I_4 I_5')

    # Definir las ecuaciones del sistema con los coeficientes corregidos
    ecuacion1 = Eq(300*I_4 + 51*I_5, 20)
    ecuacion2 = Eq(100*I_1 + 200*I_2, 20)
    ecuacion3 = Eq(100*I_1 - 150*I_3 - 300*I_4, 0)
    ecuacion4 = Eq(200*I_2 + 150*I_3 - 51*I_5, 0)
    ecuacion5 = Eq(I_1 - I_2 + I_4 - I_5, 0)

    # Resolver el sistema de ecuaciones
    solucion = solve((ecuacion1, ecuacion2, ecuacion3, ecuacion4, ecuacion5), (I_1, I_2, I_3, I_4, I_5))

    return solucion

solucion = resolver_sistema_ecuaciones()
I_1, I_2, I_3, I_4, I_5 = symbols('I_1 I_2 I_3 I_4 I_5')

print("Solución del sistema de ecuaciones:")
print("I_1 =", solucion[I_1].evalf())
print("I_2 =", solucion[I_2].evalf())
print("I_3 =", solucion[I_3].evalf())
print("I_4 =", solucion[I_4].evalf())
print("I_5 =", solucion[I_5].evalf())