import random

palavras = [
    "Relampago",
    "Horizonte",
    "Cacto",
    "Espiral",
    "Nevoa",
    "Fragmento",
    "Labirinto",
    "Marfim",
    "Pulsar",
    "Gravidade",
    "Concha",
    "Miragem",
    "Codigo",
    "Ancora",
    "Estopim",
    "Prisma",
    "Engrenagem",
    "Velo",
    "Fagulha",
    "Vortice"
]

palavra = random.choice(palavras).lower()

def jogo_da_forca():
    lista_letras = []
    for _ in palavra:
        lista_letras.append("_")

    acertou = False
    enforcou = False

    tentativas = 6

    print('--COMEÇO DO JOGO--')

    while not acertou and not enforcou:
        print(f"\nPalavra:"," ".join(lista_letras))
        print(F"Você tem {tentativas} tentativas")

        letra = input('\nDigite uma letra: ').lower().strip()

        if letra in palavra:
            print(f"Parábens!!! A letra {letra} está na palavra.")
            for l in range(len(lista_letras)):
                if palavra[l] == letra:
                    lista_letras[l] = letra
        else:
            tentativas -= 1
            print(f'OPS!!! Infelizmente {letra} não está na palavra')

        if tentativas == 0:
            enforcou = True

        if not "_" in lista_letras:
            acertou = True

    print('\n--FIM DE JOGO--')

    if acertou:
        print(f'Parabens! Você ganhou. A palavra era {palavra}')

    else:
        print(f"Você perdeu! A palavra era {palavra}")

        print('\n1 - Sim. Quero jogar novamente! \n2 - Não. Não quero jogar novamente')
    jogar_novamente = int(input('Você quer jogar novamente? '))

    if jogar_novamente == 1:
        jogo_da_forca()

    if jogar_novamente == 2:
        print('\nATÉ A PRÓXIMA!')

jogo_da_forca()

