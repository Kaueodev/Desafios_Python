quantidade = int(input("Quantos itens você deseja adicionar a sua lista? "))
print("-"*40)

lista = list(range(1, quantidade + 1))

lista_produtos = []
    
for item in lista:
    nome_produto = input('Digite o nome do produto: ')
    preco_produto = float(input('Digite o valor deste produto: '))
    print("-"*40)

    dict = {"Item": nome_produto, "Valor": preco_produto}
                                    
    lista_produtos.append(dict)

soma = 0
maior_valor = 0             
produto_mais_caro = None

for produto in lista_produtos:
    print(f"{produto['Item']} R${produto['Valor']}")
    soma += produto["Valor"] 

    if produto["Valor"] > maior_valor:
        maior_valor = produto["Valor"]  
        produto_mais_caro = produto

print(f"A soma total da lista é R${soma:.2f}")
print(F"O item mais caro da lista é: {produto_mais_caro['Item']} R${maior_valor}")
