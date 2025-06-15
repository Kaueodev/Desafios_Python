lista1 = [1, 2, 3, 4, 5, 2, 6]
lista2 = [4, 5, 6, 7, 8, 5, 4]
lista3 = []

for n in lista1:

# Aqui as duas condicoes precisam ser True (and)
    if n in lista2 and n not in lista3:
        lista3.append(n)

print(lista1)
print(lista2)
print(lista3)
