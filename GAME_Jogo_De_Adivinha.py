'''Programa que faz o computador "pensar" em um número inteiro entre 0 e 5  e pede para o usuário
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randrange
from time import sleep # faz o computador esperar em segundos
from termcolor import colored # para dar cor no seu programa

computador = randrange(0, 6) # faz o computador "PENSAR"
print(colored('-=-', 'yellow') * 20)
print('  Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(colored('-=-', 'yellow') * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
print(colored('PROCESSANDO...', 'magenta'))
sleep(3)
if jogador == computador:
    print(colored('PARABÉNS! Você conseguiu me vencer!', 'green'))
else:
    print(colored('GANHEI! Eu pensei no número {} e não no {}!', 'red').format(computador, jogador))

