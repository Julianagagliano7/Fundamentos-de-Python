def retorne_maior_e_menor(maior, menor):
    if len(menor) > len(maior):
        temp = menor
        menor = maior
        maior = temp
    return maior, menor

def achar_substring(string_1, string_2):
    maior_palavra = retorne_maior_e_menor(string_1, string_2)[0]
    menor_palavra = retorne_maior_e_menor(string_1, string_2)[1]

    maior_com_append = maior_palavra
    maior_com_append += "«" * len(menor_palavra)
    maximo_igual_char = 0
    posicao_inicial = 0

    for i in range(len(maior_palavra)):
        char_igual = 0

        for j in range(len(menor_palavra)):
            if maior_com_append[i + j] == menor_palavra[j]:
                char_igual += 1

        if char_igual > maximo_igual_char:
            posicao_inicial = i
            maximo_igual_char = char_igual

    return f'A subcadeia mais próxima tem {len(menor_palavra) - maximo_igual_char} caracteres distintos e começa na ' \
           f'posição {posicao_inicial + 1} da cadeia {maior_palavra}'

palavras = []

for i in range(2):
    palavras.append(input())

print(achar_substring(palavras[0], palavras[1]))

