numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pares = []
impares = []
impar = 0
par = 0

for i in numeros:
    if i % 2 == 0:
        par = i
        pares.append(par)
    else:
        impar = i
        impares.append(impar)

print(f"Lista de números: {numeros}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
        
