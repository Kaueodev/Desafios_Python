import random 

numero = random.randint(1, 50)

while True:

    chute = int(input('De seu chute: '))

    if chute > numero:
        print('Muito alto!')
        continue
    elif chute < numero:
        print('Muito baixo!')
        continue 
    else:
        print('Correto!')
        break
