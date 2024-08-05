# mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
_mochila = ['Computador', 'Celular', 'Memoria']

_mochila.append('Arma')
_mochila.insert(1,'canivete')
_mochila.insert(1,'bebida energetica')

_lista_referencia = _mochila[:]
_lista_referencia[0] = 'Munição'
print(f'Lista referencia: {_lista_referencia}')
print(f'Lista Original: {_mochila}')

def soma(*num):
    acumaldor = 0
    print(f'Tupla: {num}')
    for i in num:
        acumaldor += i
    return acumaldor

# for i in range(len(_mochila)):
#     print(f'Item coletado: {_mochila[i]}')