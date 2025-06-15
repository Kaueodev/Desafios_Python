frase = input('Texto: ').replace(",", "").replace(".", "").lower().split()

dict_palavra = {}

for palavra in frase:
    if palavra in dict_palavra:
        dict_palavra[palavra] += 1
    else:
        dict_palavra[palavra] = 1

print(dict_palavra)




