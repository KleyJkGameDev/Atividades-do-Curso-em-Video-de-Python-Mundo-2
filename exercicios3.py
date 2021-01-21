sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'mfMF':
    sexo = str(input('Dados inválidos! informe seu sexo: '))

print('O sexo {} foi registrado com sucesso'.format(sexo))
