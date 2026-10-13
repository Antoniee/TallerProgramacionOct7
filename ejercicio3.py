"""código original del taller:
def es_primo(n):
    for divisor in range(2, n):
        if n % divisor == 0:
            resultado = False
            break
    else:
        resultado = True
    return resultado """

"""
1)Determina qué devuelve para 1, 2 y 9, justificando si el ciclo se ejecuta y si se alcanza su else.
 Para 9, indica los divisores que se prueban.

 Para la construcción de la función es_primo(n) se tiene un ciclo for que itera sobre los divisores desde 2 hasta n-1.(así funciona
 el rango en python) y un else que se ejecuta si el ciclo termina sin encontrar un divisor que divida a n.

 * Para el caso de 1:  al quedar  range (2, 1) vacío, el ciclo no se ejecuta y se alcanza el else, devolviendo true, lo cual es un 
error porque 1 no es un numero primo. 

* Para el caso de 2:  al quedar  range (2, 2) vacío, el ciclo no se ejecuta y se alcanza el else, devolviendo true, lo cual es correcto
 porque 2 es un numero primo. 

 * Para el caso de 9:  el ciclo itera (se mueve) sobre los divisores 2,3,4,5,6,7,8. Al llegar a divisor = 3 se cumple la condición del if 
 y se asigna resultado = False y se rompe el ciclo con break. Por lo tanto no se alcanza el else y la función devuelve false,
 lo cual es correcto porque 9 no es un numero primo.

 3)Un compañero dice que el else significa «el último if fue falso». Refuta esa interpretación con uno de
 los casos anteriores. 

 * En el caso del numero 9 el if es true  al dividir por 3  y salta al break sin pasar al else.

2)Corrige la función para cumplir: «recibe un entero; devuelve False para todos los menores que 2 y decide 
primalidad para los demás». No necesitas optimizar la búsqueda ni comprobar el tipo de entrada:

 """

#Código corregido:

def es_primo(n):
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            resultado = False
            break
    else:
        resultado = True
    return resultado
