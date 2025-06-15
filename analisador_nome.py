nome = input('Digite seu nome completo: ')

mai = nome.upper()
min = nome.lower()

print(mai)
print(min)

encurtador = nome.replace(" ", "")
print(len(nome))

primeiro_nome = nome.find(" ")
print(nome[0:primeiro_nome])
