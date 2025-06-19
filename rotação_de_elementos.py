lista_original = [10, 20, 30, 40, 50, 60, 70]
posicoes = 3
nova_lista = []

fatiamento1 = lista_original[3:]

fatiamento2 = lista_original[0:3]

nova_lista = fatiamento1 + fatiamento2

print(f"Saída original: {lista_original}")
print(f"Saída rotacionada: {nova_lista}")



