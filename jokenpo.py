from random import randint
import time
computador = randint(0,2)
lista = ('PEDRA','PAPEL','TESOURA')
print("""jogadas disponiveis
[0] PEDRA
[1] PAPEL      
[2] TESOURA""")
jogador =int(input('digite as opção: '))
time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO')
time.sleep(0.8)
print(f'computador jogou {lista[computador]}')
print(f'jogador jogou {lista[jogador]}')
if computador == 0 :
    if jogador == 0 :
        print('EMPATE')
    elif jogador == 1 :
       print('VITÓRIA')
    elif jogador == 2 :
        print('DERROTA')
elif computador == 1 :
    if jogador == 0 :
        print('DERROTA')
    elif jogador == 1 : 
        print('EMPATE')
    elif jogador == 2 :
        print('VITÓRIA')
elif computador == 2 :
    if jogador == 0 :
        print('VITÓRIA')
    elif jogador == 1 :
        print('DERROTA')
    elif jogador == 2 :
        print('EMPATE')
 
