#
#===============================================================================
#
# Autor: Guilherme Sampaio Dias
#
# data 28/08/2023
#
# Exercícios para treinar o clonar a pasta do github na pasta do pc usando o git
#
#================================================================================
def media_2_valores(a,b):
    return (a+b)/2

def media_n_valores(a):
    lista = a.split()
    total  = 0
    for x in lista:
        total += int(x)
    media = total / len(lista)
    return f'A média é {media:.2f}'

def primo(x):
    if x < 2:
        return f"{x} não é primo"
    else:
        for i in range(2, int(x/2+1) ):
            if x % i == 0:
                return f'{x} não é primo'
        return f'{x} é primo'
    

