def media_2_valores(a,b):
    return (a+b)/2

def media_n_valores(a):
    lista = a.split()
    total  = 0
    for x in lista:
        total += int(x)
    media = total / len(lista)
    return f'A média é {media:.2f}'
