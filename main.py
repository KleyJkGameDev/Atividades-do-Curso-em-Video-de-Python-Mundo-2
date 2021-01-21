casa = float(input('Valor da casa R$ '))
salario = float(input('Salário do investidor R$ '))
anos = int(input('Anos de parcelamento '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

if prestacao > minimo:
    print('Investimento Negado !')
    print('Pois a prestação {:.2f} excede os 30% ({:.2f}) de seu salário {:.2f} '.format(prestacao, minimo, salario))
else:
    print('Investimento Aceito!')
    print('A prestação da casa é de {:.2f}'.format(prestacao), end='')
    print(' e seus 30% do seu salário são R{:.2f}'.format(minimo))

num = int(input('Digite um número para conversão : '))
print("Escolha a opção ")
print('[1] - Binário ')
print('[2] - Octal ')
print('[3] - Hexadecimal ')

opção = int(input('Escolha a opção : '))

if opção == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
if opção == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
if opção == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
if opção > 3 or opção < 1:
    print('Opção inválida !!')

    # ESTUDANDO WHILE
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Vc digitou {} valores pares e {} valores impares'.format(par, impar))
    break
