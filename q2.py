def f(x):
    menor = 10000000000000000000000000000000000000
    maior = 0
    for i in range(x):
        entradas = int(input('\nInforme o número de entradas: '))
        numero = int(input("Número: "))
        if numero < menor:
            menor = numero
        elif numero > maior:
            maior = numero
    return("Menor número:", menor , "Maior número:", maior)
linhas = int(input("Informe o número de linhas: "))
if linhas == 0:
    print('\nNenhum número foi lido, portanto, sem mínimo e máximo!!\n')
else:
    print(f(linhas))