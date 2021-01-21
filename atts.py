from random import randint
from time import sleep

numero = int(input('Digite um número e eu direi se é impar ou par... '))
resultado = numero % 2

if resultado == 0:
    print('O número {} é par'.format(numero))
elif resultado == 1:
    print('O número {} é ímpar'.format(numero))

computador = randint(0, 5) # Faz o computador pensar

print('-=-' * 20)
jogador = int(input('Eu pensei em um número de 0 a 5, tente adivinhar '))
print('-=-' * 20)

print('CARREGANDO...')
sleep(1)
        
if computador == jogador:
    print('-=-' * 20)
    print('Parabéns, vc acertou, eu pense i no {} e vc adivinhou!!'.format(computador))
    print('-=-' * 20)

else :
    print('=' * 20)
    print('Vc errou')
    print('Eu ganhei, eu pensei no numero {} e não no {}!'.format(computador, jogador))
    print('=' * 20)
print('fim de jogo')
