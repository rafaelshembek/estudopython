_nome_qualquer = ('rafael', 'angela', 'leila', 'rayara')
vogais = 0
for palavra in _nome_qualquer:
    print(f'\nPalavra: {palavra}. Vogais: ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra.upper()}', end='')

notas = [9,7,7,10,3,9,6,6,2]
count = 0
# print(f'Total de notas 7: {notas.count(7)}')
# print(f'A maior nota: {max(notas)}')
# notas.sort()
# print(f'Notas ordenadas: {notas}')
# print(f'A media das notas: {sum(notas) / len(notas)}')
