from datetime import date

data = int(input('Em que ano estamos ?( digite 0 pra saber a data atual) '))

if data == 0 :
    data = date.today().year
    
if data % 4 == 0 and data % 100 != 0 or data % 400 == 0 :
    print('O ano é Bissesxto!')
else:
    print('O ano não é bissexto')
    
km = float(input('Qual a distância de sua viajem ? ')) #KM rodados

if km <= 200:
    preço = (km * 0.50)

else:
    preço = (km * 0.45)

'''# preço = km * 0.50 if <=200 else km * 0.45'''

print('O preço de sua viajem é de {}R$'.format(preço))   
print('Tenha uma boa viajem ')
