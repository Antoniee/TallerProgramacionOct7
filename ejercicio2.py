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