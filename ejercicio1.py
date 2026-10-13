""""
Código original del taller: 

total = 0.0
cantidad = 0
while True:
    texto = input("Medición o fin: ")
    valor = float(texto)
    if texto == "fin":
        break
    if valor >= 0:
        total += valor
    cantidad += 1
print(total / cantidad)"""

""" Primero: Al realizar la primera indicación del taller obtengo esto: 
antonia_cardozo@LAPTOP-J24T25G4:~/Programacion/Clases/talleres/tallerOct$ /usr/bin/python3 /home/antonia_cardozo/Programacion/Clases/talleres/tallerOct/ejercicio1.py
Medición o fin: 4
Medición o fin: -2
Medición o fin: 6
Medición o fin: fin
Traceback (most recent call last):
  File "/home/antonia_cardozo/Programacion/Clases/talleres/tallerOct/ejercicio1.py", line 5, in <module>
    valor = float(texto)
ValueError: could not convert string to float: 'fin'
antonia_cardozo@LAPTOP-J24T25G4:~/Programacion/Clases/talleres/tallerOct$ 



Segundo: Corrige el programa para que reconozca fin, rechace entradas no numéricas con un mensaje y continúe solicitando datos. 
Los valores negativos no deben entrar en la suma ni en el contador. Si no se aceptó ninguna medición,
debe informar esa situación sin dividir:

a) Como primer Error identifico que el programa intenta convertir "fin" a un número decimal,
 lo cual causa un error. La solución es verificar si el texto es "fin" antes de intentar la conversión
 
 De esta Manera: 
total = 0.0
cantidad = 0
while True:
    texto = input("Medición o fin: ")
    if texto == "fin":
        break
    valor = float(texto)
    if valor >= 0:
        total += valor
    cantidad += 1
print(total / cantidad)

b) Agrego un except value error + un continue
total = 0.0
cantidad = 0
while True:
    texto = input("Medición o fin: ")
    if texto == "fin":
        break
    valor = float(texto)
    try:
        valor = float(texto)
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        continue
    if valor >= 0:
        total += valor
    cantidad += 1
print(total / cantidad)

c)Idento cantidad += 1 y  Agrego  un else para cantidades negativas 

if valor >= 0:
        total += valor
        cantidad += 1
else:
    print("Error: Ingrese un valor numérico positivo.")

d) Evitar división por cero:

if cantidad > 0:
    print(total / cantidad)
else:
    print("No se aceptó ninguna medición válida.")


3) Explica por qué cambiar float(texto) por eval(texto) 
    no es una corrección adecuada para el contrato «recibir una medición numérica»:
 Cambiar `float(texto)` por `eval(texto)` ya que como vimos en clase es un comando peligroso que puede ejecutar cualquier código, 
 o código arbitrario, podría leer un script de malware, además de no ser eficiente"""

#código Corregido:

total = 0.0
cantidad = 0
while True:
    texto = input("Medición o fin: ")
    if texto == "fin":
        break
    
    try:
        valor = float(texto)
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        continue
    if valor >= 0:
        total += valor
        cantidad += 1
    else:
        print("Error: Ingrese un valor numérico positivo.")

if cantidad > 0:
        print(total / cantidad)
else:
    print("No se aceptó ninguna medición válida.")

