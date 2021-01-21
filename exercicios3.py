from random import randint
from time import sleep
from math import factorial

tabela2 = 1

while tabela2 == 1:
    print('')
    print('''[1] Validação de Dados
[2] Jogo da Adivinhação 2.0
[3] Criando um menu de opções
[4] Cálculo do fatorial
[5] Progressão aritmética
[6] Super progressão aritmética
[7] Sequência de Fibonacci
[8] Tratando vários valores
[9] Maior e menor valores
[0] Sair''')
    escolha = int(input('Escolha a opção que deseja: '))

    # Validação de Dados
    if escolha == 1:
        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
        while sexo not in 'mfMF':
            sexo = str(input('Dados inválidos! informe seu sexo: '))

        print('O sexo {} foi registrado com sucesso'.format(sexo))

    # Jogo da Adivinhação v.2.0
    elif escolha == 2:
        sort1 = randint(0, 10)
        cont1 = 0
        print(sort1)
        print('O computador pensou em um número entre 0 e 10')
        sort = int(input('Tente adivinhar o número que pensei: '))
        while sort != sort1:
            sort = int(input('Errou!! Tente de novo: '))
            cont1 += 1
            if sort < sort1:
                print('Está perto! Tente um valor mais alto')
            elif sort > sort1:
                print('Quase! Tente um valor menor')

        print('Acertou! O número que pensei foi {}'.format(sort1))
        print('Vc fez {} tentativas'.format(cont1))

    # Criando um menu
    elif escolha == 3:
        menu3 = 1
        while menu3 == 1:
            print('')
            print('''[1] Soma
[2] Maior
[3] Multiplicação
[4] Novos números
[5] Sair''')
            num31 = int(input('Digite um valor: '))
            num32 = int(input('Digite outro valor: '))
            escmenu = int(input('Escolha uma das opções: '))

            if escmenu == 1:
                print('{} + {} = {}'.format(num31, num32, num31 + num32))
            elif escmenu == 2:
                if num31 > num32:
                    print('{} é o maior número'.format(num31))
                elif num32 > num31:
                    print('{} é o maior número'.format(num32))
            elif escmenu == 3:
                print('{} x {} = {}'.format(num31, num32, (num31 * num32)))
            elif escmenu == 4:
                print('Carregando...')                 
            elif escmenu == 5:
                print('Saindo...')
                sleep(0.5)
                break

    # Cálculo Fatorial
    elif escolha == 4:
        menu4 = 1
        num4 = int(input('Digite um valor para ver o fatorial: '))
        cont4 = num4
        fac4 = factorial(num4)
        tot4 = 0
        print('O fatorial de {} é {}'.format(num4, fac4))
        while cont4 > 0:
            print('{}'.format(cont4), end='')
            print(' x ' if cont4 > 1 else ' = ', end='')
            cont4 -= 1            
        print('{}'.format(fac4))
            
    # Progressão Aritmética
    elif escolha == 5:
        term5 = int(input('Digite o primeiro termo: '))
        raz5 = int(input('Digite a razão: '))
        termo5 = term5
        cont5 = 1
        while cont5 < 11:
            print('{} -> '.format(termo5), end='')
            termo5 += raz5
            cont5 += 1
        print('fim')

    # Super Progressão v3.0
    elif escolha == 6:
        term6 = int(input('Digite o primeiro termo: '))
        raz6 = int(input('Digite a razão: '))
        termo6 = term6
        cont6 = 1
        tot6 = 0
        mais6 = 10
        while mais6 != 0:
            tot6 = tot6 + mais6
            while cont6 <= tot6 :
                print('{} -> '.format(termo6), end='')
                termo6 += raz6
                cont6 += 1
            print('PAUSA')
            mais6 = int(input('Quantos valores a mais: [0] para sair  '))
        print('Programa finalizado com {} termos mostrados'.format(tot6))

    # Sequência de Fibonacci
    elif escolha == 7:
        print('-='*30)
        print('FIbonacci')
        num7 = int(input('Digite quantos termos quer mostrar: '))
        t17 = 0
        t27 = 1
        print('{} -> {}'.format(t17, t27), end='')
        cont7 = 3
        while cont7 <= num7:
            t37 = t17 + t27
            print(' -> {}'.format(t37), end='')
            t17 = t27
            t27 = t37
            cont7 += 1
        print(' FIM')

    # Tratando Valores
    elif escolha == 8:
        cont8 = tot8 = num8 = 0
        while num8 != 999:
            num8 = int(input('Digite um valor: [999] para sair '))
            cont8 += 1
            tot8 += num8
        print('{} valores registrados, soma total {}'.format(cont8, tot8 - num8))

    # Maior e menor
    elif escolha == 9:
        maior9 = menor9 = tot9 = num9 = cont9 = 0 
        print('-='*20)
        num9 = int(input('Digite qualquer coisa para continuar '))
        while num9 != 0:
            num9 = int(input('Digite um valor: [0] para sair '))
            cont9 += 1
            tot9 += num9
            if num9 == 1:
                maior9 = num9
                menor9 = num9
            else:
                if num9 > maior9:
                    maior9 = num9
                elif num9 < menor9:
                    menor9 = num9
        print('O maior valor é {} e o menor {}'.format(maior9, menor9))
        print('A média entre eles é {:.2f}'.format((tot9 / cont9)))


    # Valor inválido
    elif 0 > escolha > 9:
        print('Opção inválida!!!')

    # Sair do Programa
    elif escolha == 0:
        print('Saindo...')
        sleep(1.0)
        break

    