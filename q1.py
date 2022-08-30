
numero = input('\nDigite um número: ')
soma = 0.0
cont = 0

while numero != '':
    soma += float(numero)
    numero = input('\nDigite um número: ')
    cont += 1

if cont == 0:
    print('\nNenhuma linha lida com conteúdo, portanto não há soma nem média!\n')
if cont > 0:
    media = soma/cont
    print('\nSoma dos Números: {:.2f}\n' .format(soma))
    print('\nMédia dos Números: {:.2f}\n'.format(media))

