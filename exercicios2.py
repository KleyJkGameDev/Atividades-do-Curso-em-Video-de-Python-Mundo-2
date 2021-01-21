from time import sleep
from datetime import date
# A contagem para no ultimo item. ex: range(0, 4) --> 1, 2, 3
# para contagem regressiva use --> range(4, 0, -1)
# uma terceira virgula serve para iteração --> renge(0, 4, 2) --> 0, 2, 4

programa = 0
while programa == 0:
    print('\n')
    print('''[1] Contagem regressiva
[2] Contagem de Pares
[3] Soma ímpares e multiplos de 3
[4] Tabuada v2.0
[5] Soma dos pares
[6] Progressão aritimética
[7] Números primos
[8] Detector de palíndromos
[9] Grupo da maioridade
[10] Maior e menor da sequencia
[11] Analisador completo
[12] Sair''')
    escolha = int(input('Escolha sua opção: '))

    #Contagem Regressiva
    if escolha == 1:
        print('tempo para lancamento de fogos de artificios...')

        for c in range(10, -1, -1):
            print(c)
            sleep(0.2)

        print('Fogos Lançados !!!')
        sleep(1)
        print('-='*15)

    #Contagem em pares
    elif escolha == 2: 
        for c2 in range(0, 51, 2):
            print(c2, end=' .')

    #Soma Ímpares e multiplos de 3
    
    elif escolha == 3:
        soma3 = 0
        cont3 = 0
        for c3 in range(1, 501, 2):
            if c3 % 3 == 0:
                soma3 += c3
                cont3 += 1
        print('A soma de todos os {} valores é {}'.format(soma3, cont3))

    #Tabuada v2.0
    elif escolha == 4:

        print('''[1] Adição
[2] Subtração
[3] Multiplcação''')
        tabu = int(input('Escolha um número para mostrar a tabuada: '))
        tabela = int(input('Escolha qual tabuada deseja mostrar: '))

        if tabela == 1:
            for tabuc in range(0, 10):
                adc = tabuc + 1
                print(tabu, '+', tabuc + 1, '=', tabu + adc)

        elif tabela == 2:
            for tabuc in range(0, 10):
                sub = tabuc + 1
                print(tabu, '-', tabuc + 1, '=', tabu - sub)

        if tabela == 3:
            for tabuc in range(0, 10):
                mult = tabuc + 1
                print(tabu, 'x', tabuc + 1, '=', tabu * mult)

    #Soma dos Pares
    elif escolha == 5:
        soma5 = 0
        cont5 = 0
        for c5 in range(1,7):
            num5 = int(input('Digite o {}º número: '.format(c5)))
            if num5 % 2 == 0:
                soma5 += num5
                cont5 += 1
        print('A soma dos {} valores pares é {}'.format(cont5, soma5))

    #Progressão Aritmética
    elif escolha == 6:
        print('='*20)
        print('10 Termos de um PA')
        print('='*20)
        term6 = int(input('Primeiro termo: '))
        raz6 = int(input('Razão: '))
        dec6 = term6 + (10 - 1) * raz6
        for c6 in range(term6, dec6 + raz6, raz6):
            print('{}'.format(c6), end=' -> ')
        print('\n')

    # Números Primos
    elif escolha == 7:
        num7 = int(input('Digite um número: '))
        tot7 = 0
        for c7 in range(1, num7 + 1):
            if num7 % c7 == 0:
                print('{}'.format(c7, end=' -> '))
                tot7 += 1
            else:
                print('')
        print('O numero {} foi divisivel {} vezes'.format(num7, tot7))
        if tot7 == 2:
            print('O número {} é primo'.format(num7))        
        print('\n')

        if tot7 > 2 or tot7 < 2:
            print('O número {} não é primo'.format(num7))

    # Palíndromo
    elif escolha == 8:
        frase8 = str(input('Digite uma frase: ').strip().upper())
        print(' ')
        palavras8 = frase8.split()
        junto8 = ''.join(palavras8)
        inver8 =''

        for letra8 in range(len(junto8) -1, -1, -1):
            inver8 += junto8[letra8]
        
        print(junto8, inver8)
        if junto8 == inver8:
            print('A frase {} é um palíndromo!'.format(frase8))
        else:
            print('A frase {} não é um palíndromo'.format(frase8))
        print(' ')

    # Maioridade
    elif escolha == 9:
        atual9 = 2021
        totmaior9 = 0
        totmenor9 = 0
        for c9 in range(1, 8):
            ano9 = int(input('{}º Data de nascimento: '.format(c9)))
            idade = atual9 - ano9
            print('Vc nasceu em {}'.format(ano9))

            if idade >= 18:
                totmaior9 += 1
                print('Sua idade é {}, vc é maior de idade!'.format(idade))
            else:
                totmenor9 += ''
                print('Sua idade é {}, vc ainda não é maior de idade!'.format(ano9 - atual9))
        print('Totalde maiores de idade: {}'.format(totmaior9))
        print('Total de menores de idade: {}'.format(totmenor9))
        print(' ')

    # Maior e menor
    elif escolha == 10:
        maior10 = 0
        menor10 = 0
        for p10 in range(1, 6):
            peso10 = float(input('O {}º Peso: '.format(p10)))
            if p10 ==1:
                maior10 = peso10
                menor10 = peso10
            else:
                if peso10 > maior10:
                    maior10 = peso10 
                elif peso10 < menor10:
                    menor10 = peso10
        print('O maior peso lido foi de {} Kg'.format(maior10))
        print('O menor peso lido foi de {} Kg'.format(menor10)) 
        print('\n')

    # Analisador completo
    elif escolha == 11:
        cont11 = 0
        contmulher11 = 0
        maior11 = 0
        maisvelho = ''
        for c11 in range(1, 6):
            print('-------- {}º PESSOA --------'.format(c11))
            nome11 = str(input('Nome: '.strip()))
            idade11 = int(input('Idade: '))
            sexo11 = str(input('Sexo [M/F]: '))
            cont11 += idade11
            if maior11 == 1 and sexo11 in 'MmnN':
                maior11 = idade11
                maisvelho11 = nome11
            elif sexo11 in 'MmnN' and idade11 > maior11:
                maior11 = idade11
                maisvelho = nome11
            elif sexo11 in 'Ff' and idade11 < 20:
                contmulher11 += 1
                
        print('A média de idade das pessoas é {}'.format(cont11 / c11))
        print('O homem mais velho tem {} anos e se chama {}'.format(maior11, maisvelho))
        print('Existem {} mulheres com menos de 20 anos'.format(contmulher11))

    # FIM DO PROGRAMA
    elif escolha == 12:
        print('Saindo...')
        sleep(1.3)
        break

