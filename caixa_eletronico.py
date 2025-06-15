saldo = float(0)

while True:
    print("Opção 1 - Ver saldo")
    print("Opção 2 - Depositar")
    print("Opção 3 - Sacar")
    print("Opção 4 - Sair")

    opcao = int(input("Selecione a opção que deseja: "))

    if opcao == 1:
        print(f'R${saldo}')

        print('\n1 - Sim \n2 - Não')
        voltar = int(input('Deseja voltar ao menu inicial? '))
        if voltar == 1:
            continue
        else:
            print('Até a próxima!')
            break
    elif opcao == 2:
        deposito = float(input('Quanto você deseja depositar? R$'))
        soma_deposito = saldo + deposito
        saldo = soma_deposito
        print(f'Deposito efetuado com sucesso!')

        print('\n1 - Sim \n2 - Não')
        voltar = int(input('Deseja voltar ao menu inicial? '))
        if voltar == 1:
            continue
        else:
            print('Até a próxima!')
            break
    elif opcao == 3:
        saque = float(input("Quanto você deseja sacar? R$"))
        if saldo < saque:
            print('Saldo insuficiente!')
        else:
            soma_saque = saldo - saque
            print(f'Saque efetuado com sucesso')

        print('\n1 - Sim \n2 - Não')
        voltar = int(input('Deseja voltar ao menu inicial? '))
        if voltar == 1:
            continue
        else:
            print('Até a próxima!')
            break

    elif opcao == 4:
        print('Até a próxima!')
        break        

