entrada = "a123bc34d8ef34"
identificador = []
digito = ""

for i in entrada:
    if i.isdigit():
        digito += i
    else:
        if digito != "":
            identificador.append(int(digito))
            digito = ""

if digito != "":
    identificador.append(int(digito))

num = []
saida = 0

for i in identificador:
    if not i in num:
        num.append(i)
        tamanho = len(num)
        saida = tamanho

print(saida)

