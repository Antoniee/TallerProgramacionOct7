# 4. Recursividad: contrato, caso base y progreso
#Se consideran entradas enteras en ambos fragmentos:

"""
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


def euclides(a, b):
    if b == 0:
        return a
    return euclides(b, a % b)
    """

"""
1)Escribe la secuencia de llamadas de euclides(84, 30) hasta el caso base y el valor que se devuelve.
 Explica qué cantidad disminuye y por qué termina para esos argumentos.

Primera llamada: euclides(84, 30)
Segunda llamada: euclides(30, 84 % 30) = euclides(30, 24)
Tercera llamada: euclides(24, 30 % 24) = euclides(24, 6)
Cuarta llamada: euclides(6, 24 % 6) = euclides(6, 0)

La función busca el MCM entre dos números, para este caso se busca el mcm entre 84 y 30,  la función llama al código hasta que encuentra 
número que no tenga residuo, en este caso el 6, que es el MCM entre 84 y 30, para ello se usa la función % modulo de la división. 

2)La primera función parece funcionar con 0 y 4. ¿Por qué esos casos no bastan para verificar el 
contrato «factorial de un entero no negativo»? Corrígela para rechazar entradas negativas mediante ValueError.

Para verificar el contrato debería testearse con un número negativo, ya que el factorial de un número negativo no está definido,
sin embargo debido a que el código tiene un caso base que devuelve 1 para n <= 1, si entraramos por ejemplo -3 el código no fallaríaon
y devolvería 1  por lo que no cumple con el contrato.

3) Para factorial(4), distingue llegar al caso base de terminar toda la ejecución: muestra las multiplicaciones pendientes 
al llegar al caso base. No se pide convertirla a una versión iterativa.

"""

#Código corregido:
def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    return 1 if n <= 1 else n * factorial(n - 1)        