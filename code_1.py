print('Hello Mundo')
from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador 'PENSAR'
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente aidvinhar...')
jogador = int(input('Em que número pensei? ')) # Jogaodr tenta adivinhar
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('GANHEI! Pensei no {} e não no {}.'.format(computador, jogador))

print('Finalisando o codigo')


