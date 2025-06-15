
vendas = [
    {'produto': 'arroz', 'valor': 25.00},
    {'produto': 'feijão', 'valor': 8.50},
    {'produto': 'arroz', 'valor': 24.30},
    {'produto': 'macarrão', 'valor': 5.20},
    {'produto': 'feijão', 'valor': 8.00},
    {'produto': 'carne', 'valor': 55.00},
    {'produto': 'arroz', 'valor': 26.20},
]

soma = 0
sum_vendas = {}

for valor in vendas:
    soma += valor["valor"]

print(f'A soma total dos valores vendidos foi: R$ {soma}')

for dict in vendas:
    chave = dict["produto"]
    valor = dict["valor"]
    if chave in sum_vendas:
        sum_vendas[chave] += valor
    else:
        sum_vendas[chave] = valor

print(f"Total vendido para cada item: {sum_vendas}")


lista = list(sum_vendas.values())
maior = max(lista)

for produto, valor in sum_vendas.items():
    if valor == maior:
        print(f"O produto que mais vendeu em valores: {produto} R$ {maior}")





