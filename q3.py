frase = "b"
mais_vogal = 0
mais_palindromos = 0

def conta_vogal(string):
    string = string.lower()
    result = 0
    letra_vog = 'aeiou'
    for i in letra_vog:
        result += string.count(i)
    return result

def conta_palavra(string):
    result = len(string)
    return result

def maior_palavra_na_frase(string):
    lista_palavras = list(string.split(" "))
    maior_palavra = max(lista_palavras, key=len)
    return maior_palavra

def verifica_palindromo(string):
    lista_palindromos = list(string.split(" "))
    qtd_palindromo = 0
    for palindromo in lista_palindromos:
        is_palindromo = palindromo == palindromo[::-1]
        if is_palindromo:
           qtd_palindromo += 1
    return qtd_palindromo


while(frase):
    frase = input("\nDigite uma frase:")

    palindromos = verifica_palindromo(frase)

    if frase:
        qtd_vog = conta_vogal(frase)
        qtd_letras = conta_palavra(frase)

    if(qtd_vog > mais_vogal):
        mais_vogal = qtd_vog
        frase_mais_vogais = frase

    if(palindromos > mais_palindromos):
        mais_palindromos = palindromos
        frase_mais_palindromos = frase

print("\nLinha com mais vogais sem acento: ", frase_mais_vogais)
print("\nQuantidade de vogais sem acento:  ",mais_vogal,)
print("\nPalavra de maior comprimento lida: ", maior_palavra_na_frase(frase_mais_vogais))
print("\nLinha com mais Palíndromos: ", frase_mais_palindromos)
print('\nQuantidade de palavras Palíndromas: ', mais_palindromos)

