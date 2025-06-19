def bubble(lista):
    n = len(lista)
    for final in range(n - 1):
        troca = False

        for atual in range(0, n - final - 1):
            if lista[atual] > lista[atual + 1]:
                lista[atual], lista[atual + 1] = lista[atual + 1], lista[atual]
                troca = True
        if not troca:
            break


lista = [9, 8, 7, 3, 2, 5, 10, 20, 21]
bubble(lista)
print(lista)



