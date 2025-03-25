from random import randint 
jogadas = ["PEDRA" ,"PAPEL" ,"TESOURA"]
computador = randint(0,2)
print("""Escolha suas jogadas
[PEDRA] 0
[PAPEL] 1
[TESOURA] 2""")
jogador = int(input('Digite a opção: '))
print(f'Computador jogou {jogadas[computador]}')
print(f'Jogador jogou {jogadas[jogador]}')
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VITÓRIA')   
    elif jogador == 2:
        print('DERROTA')
elif computador == 1:
    if jogador == 0:
        print('DERROTA')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VITÓRIA')   
elif computador == 2:
    if jogador == 0:
        print('VITÓRIA')
    elif jogador == 1:
        print('DERROTA')
    elif jogador == 2:
        print('EMPATE')   
#{jogadas[computador]}
#lista a jogada que o computador pode jogar 
