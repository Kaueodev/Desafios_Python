dict = {"Ipad": 6000, "macbook":15000, "iphone": 9000}

nome_produto = input('Digite o nome do produto: ').lower()
preco_produto = int(input("Digite o preço do produto: "))

novo_produto = dict[nome_produto] = preco_produto

print(dict)

for produto in dict:
    produto = produto
    novo_preco = dict[produto] * 1.1
    dict[produto] = novo_preco

print(dict)
