from time import sleep
from random import randint
opção = 0

while opção == 0:
    print('''[1] Maior e menor
[2] Alistamento Militar
[3] Media do aluno
[4] Atletas
[5] Triângulo
[6] IMC
[7] Gerenciador de pagamentos
[8] Joken Pô!
[9] sair''')

    tabela = int(input('Escolha a opção: '))

    #MAIOR E MENOR
    if tabela == 1:

        num = int(input('digite um numero '))
        num2 = int(input('Digite outro numero '))

        if num > num2:
            print('O maior número é {}'.format(num))
            print('O mennor número é {}'.format(num2))
            print('Os dois números são diferentes')
        if num < num2:
            print('O maior número é {}'.format(num2))
            print('O mennor número é {}'.format(num))
            print('Os dois números são diferentes')
        else:
            print('Não existe numero maior ou menor, os dois são iguais')
        sleep(2)
        
    #ALISTAMENTO
    elif tabela == 2:

        ano = int(input('Idade do jovem : '))
        if ano < 17:
            print('Vc ainda é novo pra se alistar!')
            print('Tempo restante para se alistar {}'.format(17 - ano))
        if ano > 17:
            print('Vc passou do tempo para se alistar!')
            print('Tempo de atraso {} anos'.format(ano - 17))
        elif ano == 17:
            print('Vc deve se alistar agora !!')
        sleep(2)

    #MEDIA
    elif tabela == 3:

        nota1 = float(input('Primeira nota : '))
        nota2 = float(input('Segunda nota : '))
        media = (nota1 + nota2) / 2

        if media > 6.0:
            print('Parabéns, vc foi aprovado!!')
            print('Média : {:.2f}'.format(media))
        if media < 5.0:
            print('BURRO! Vc foi reprovado!')
            print('Média : {:.2f}'.format(media))
        elif 5.0 < media < 6.0:
            print('Vc está de recuperação com média {:.2f}'.format(media))
        sleep(2)

    #ATLETA
    elif tabela == 4:

        idade = int(input('Digite sua idade : '))

        if idade >= 0 and idade <= 9:
            print('Vc é um atleta mirim!')
        elif idade >= 10 and idade <= 14:
            print('Vc é um atleta infantil!')
        elif idade >= 15 and idade <= 19:
            print('Vc é um atleta júnior!')
        elif idade >= 20 and idade <= 25:
            print('Vc é um atleta sênior!')
        elif idade < 0:
            print('Essa idade é invalida')
        elif idade > 25:
            print('Vc é um atleta master!')
        sleep(2)


    #Analisando triângulos
    elif tabela == 5:
        r1 = int(input('Primeiro segmento : '))
        r2 = int(input('Primeiro segmento : '))
        r3 = int(input('Primeiro segmento : '))

        if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
            print('Os segmentos Podem formar um triângulo!')
            if r1 == r2 == r3:
                print('Triângulo Equilátero')
            elif r1 != r2 != r3 != r1:
                print('Triângulo Escaleno!')
            else:
                print('Triângulo Isóceles!')
        else:
            print('Os segmentos não podem formar um triãngulo!')
        sleep(2)
    #IMC
    if tabela == 6:
        peso = float(input('Peso da pessoa : '))
        altura = float(input('A altura : '))
        imc = peso / altura

        if imc < 18.5:
            print('Vc está abaixo do peso com IMC {:.2f}'.format(imc))
        elif 25 <= imc >= 18.5:
            print('Vc está no peso ideal com IMC {:.2f}'.format(imc))
        elif 25 < imc < 30:
            print('Vc está com sobrepeso com IMC {:.2f}'.format(imc))
        elif 30 <= imc >= 40:
            print('Vc está com Obesidade com IMC {:.2f}'.format(imc))
        else:
            print('Vc está com Obesidade Mórbida com IMC {:.2f}'.format(imc))
        sleep(2)

    #Gerenciador de Pagamentos
    elif tabela == 7:
        valorcompra = float(input('Valor da compra R$'))
        print('''[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
        escolha = int(input('Escolha o modo de pagamento : '))

        if escolha == 1:
            desconto1 = valorcompra * 10 / 100
            valorfinal1 = valorcompra - desconto1
            print('O valor final da compra é de R${}, com desconto de R${}'.format(valorfinal1, desconto1))
            print('Volte sempre !!!')

        elif escolha == 2:
            desconto2 = valorcompra * 5 / 100
            valorfinal2 = valorcompra - desconto2
            print('O valor final da compra no cartão é de R${}, com R${} de desconto'.format(valorfinal2, desconto2))
            print('Volte sempre !!!')

        elif escolha == 3:
            parcelas = int(input('Numero de parcelas : '))
            desconto3 = valorcompra + 0
            parcelamento = valorcompra / parcelas

            if parcelas >= 2:
                print('O valor da compra é de R${} por {} parcelas'.format(parcelamento, parcelas))
                print('Volte sempre !!!')

            elif parcelas >= 3:
                juros = valorcompra * 20 / 100
                valorfinal3 = valorcompra + juros

                print('O valor final da compra é de R${}, com R${} de juros'.format(valorfinal3, juros))
                print('Volte sempre !!!')

        elif escolha == 4:
            juros2 = valorcompra * 20 / 100
            valorfinal4 = valorcompra + juros2

            print('O valor final da compra é de R${}, com R${} de juros'.format(valorfinal4, juros2))
            print('Volte sempre !!!')
        else:
            print('Escolha inválida')
        sleep(2)

    # GAME Pedra, papel, tesoura
    elif tabela == 8:
        itens = ('nada', 'Pedra', 'Papel', 'Tesoura')
        maquina = randint(1, 3)
        print('='*15)
        print('''[1] Pedra
[2] Papel
[3] Tesoura''')
        print('='*15)
        jogador = int(input('Escolha sua jogada: '))

        if maquina == jogador:
            print('EMPATE !!!')

        elif maquina == 1 and jogador == 3:
            print('O computador venceu !!!')
        
        elif maquina == 2 and jogador == 1:
            print('O computador venceu !!!')
        
        elif maquina == 3 and jogador == 2:
            print('O computador venceu !!!')

        else:
            print("VENCEU MIZERAVI!!")
        print('='*15)
        print("O computador escolheu {}".format(itens[maquina]))
        
        print("Você escolheu {}".format(itens[jogador]))
        print('='*15)
        sleep(2.5)

    elif tabela == 9:
        print('SAINDO.....')
        sleep(2)
        break
    else:
        print('Escola inválida!!')
        sleep(2)
    

