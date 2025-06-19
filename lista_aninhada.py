lista_aninhada = [[5, 9, 4], [1, 2], [7, 6, 3, 8]]
lista_achada = []

for i in lista_aninhada:
    for i2 in i:
        lista_achada.append(i2)

print(sorted(lista_achada))
