turma = {
    'Ana': [8.0, 9.0, 10.0],
    'Bruno': [4.5, 6.0, 7.5],
    'Carla': [7.0, 7.0, 7.0],
    'Daniel': [10.0, 10.0, 5.0],
}

print('Relatório da turma:')
print('-'*5)

media = 0

for chave, nota in turma.items():
    
    soma = sum(nota)
    tamanho = len(nota)
    media = soma / tamanho

    print(f'Aluno: {chave}')
    print(f'Notas: {nota}')
    print(f'Média: {media:.1f}')

    if media <= 7:
        print('Status: Reprovado')
    else:
        print('Status: Aprovado')

    print('-'*5)
