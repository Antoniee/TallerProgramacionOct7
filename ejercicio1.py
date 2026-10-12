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
print(total / cantidad)g