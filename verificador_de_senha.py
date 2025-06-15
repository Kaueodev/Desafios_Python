while True:
    
    senha = input("Digite a senha desejada: ")

# Variaveis de controle (flags)
    tem_maiuscula = False
    tem_numero = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.isdigit():
            tem_numero = True

    if len(senha) < 8:
        print("ERRO: A senha deve ter no mínimo 8 caracteres. Tente novamente.")
        continue 
    elif not tem_maiuscula:
        print("ERRO: A senha deve conter pelo menos uma letra maiúscula. Tente novamente.")
        continue
    elif not tem_numero:
        print("ERRO: A senha deve conter pelo menos um número. Tente novamente.")
        continue
    else:
        print("Senha válida!")
        break

while True:
    confirmacao_senha = input("Digite a senha novamente para confirmar: ")
    
    if confirmacao_senha == senha:
        print("🎉 Senha definida com sucesso!")
        break 
    else:
        print("ERRO: As senhas não coincidem. Tente novamente.")
        continue
    
    

    







