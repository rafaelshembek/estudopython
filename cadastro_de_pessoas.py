cadastro = {'nome': [], 'sexo': [], 'ano': []}

while True:
    _terminar = input('Deseja cadastra uma pessoa? [S/N]')
    if _terminar.upper() in 'N':
        break
    if _terminar.upper() not in 'S':
        print(f'Digite S para SIM ou N para NÃO.')
        continue

    _nome = input('Nome? ')
    _sexo = input('Sexo? ')
    _ano = input('Ano? ')
    cadastro['nome'].append(_nome)
    cadastro['sexo'].append(_sexo.upper())
    cadastro['ano'].append(_ano)
print(cadastro)