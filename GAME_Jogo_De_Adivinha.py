'''Melhorando o jogo, onde o computador vai "pensar" em um número entre 0 a 10 que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários.'''
from random import randint
from time import sleep # faz o computador esperar em segundos
from termcolor import colored # para dar cor no seu programa

print(colored('-=-', 'yellow') * 20)
print('  Ola! Sou seu computador, Vamos jogar?')
print('  Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print(colored('-=-', 'yellow') * 20)
computador = randint(0, 10)  # faz o computador "PENSAR"
acertou = False
palpite = 0

while not acertou:
    palpite += 1
    jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
    print(colored('PROCESSANDO...', 'magenta'))
    sleep(1)
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez! ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez! ')
print(colored('PARABÉNS! Você conseguiu acertar com {} tentativas!', 'green').format(palpite))
