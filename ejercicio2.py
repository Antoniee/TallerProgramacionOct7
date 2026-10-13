"""Código original del taller:
def registrar(valores, registro):
    copia = valores.copy()
    copia[0] = copia[0] + 1
    registro["ultima"] = copia
    return copia

datos = [2, 4]
registro = {}
salida = registrar(datos, registro)
salida.append(8)
print(datos)
print(registro)
print(salida)



1) Predice las tres salidas. Identifica qué objetos son distintos y qué nombres o entradas del diccionario
 apuntan a la misma lista. ¿Copiar valores evita todas las modificaciones compartidas de este programa?

 a) Salida del código original:
Imprime primero la variable datos que es una lista:
[2, 4]

Luego imprime registro como diccionario con la clave "ultima" y el valor de la lista copia, en la cual se  suma 1 al valor
de la posición 0  que  es 2 y se le agrega un 8 con el comando salida.append(8) que modifica la lista copia:
{'ultima': [3, 4, 8]}

Por útlimo imprime la variable salida que es la lista copia con el valor modificado en la posición 0 y el 8 agregado al final:
[3, 4, 8]

b) Los objetos distintos son:
datos: [2, 4] y salida: [3, 4, 8] son listas distintas.
ultima es una clave del diccionario registro que apunta a la misma lista que salida, por lo tanto, apuntan a la misma lista.

c) ¿Copiar valores evita todas las modificaciones compartidas de este programa?
en realidad copiar valores evita que la lista original datos se modifique, pero no evita que la lista copia se modifique, 
ya que salida y registro["ultima"] apuntan a la misma lista copia entonces se afectan mutuamente

2.Cambia únicamente la asignación a registro["ultima"] para que modificaciones posteriores de salida no cambien 
lo almacenado en el registro. Justifica por qué basta en este caso de números.

a) La idea es crear una lista diferente entonces usaré  la siguiente asignación:
registro["ultima"] = copia.copy()
Esto es suficiente porque los elementos de la lista son números, que son inmutables, entonces no se modificarían por los nuevos valores.

3) Si datos fuera la tupla (2, 4), señala la primera operación que fallaría. Propón un cambio en la creación de copia
 que permita recibir lista o tupla conservando el resto de la función.

 a) La primera parte del código que fallaría sería la línea copia[0] = copia[0] + 1, ya que las tuplas son inmutables y no se puede modificar un elemento de una tupla.
 
 """