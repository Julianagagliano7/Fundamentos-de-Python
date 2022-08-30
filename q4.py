def n_inteiro(numero):
    todos_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
    for n in numero:
        if n not in todos_numeros:
            return False
    return True


def exponenciacao(base_, expoente_):
    if base_ is not None and expoente_ is not None:
        resultado = int(base_) ** int(expoente_)
        return resultado
    base = input()
    expoente = input()
    if base_ is None and expoente_ is None:
        if n_inteiro(base) and n_inteiro(expoente):
            return f'{base} elevado a {expoente} é igual a {exponenciacao(base, expoente)}'
        elif not n_inteiro(base) and not n_inteiro(expoente):
            return f'Base {base} e expoente {expoente} não estão no formato devido'
        elif not n_inteiro(base):
            return f'Base {base} não está no formato devido'
        elif not n_inteiro(expoente):
            return f'Expoente {expoente} não está no formato devido'


print(exponenciacao(None, None))

