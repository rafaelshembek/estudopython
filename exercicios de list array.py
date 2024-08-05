mochila = [['Cebola', 0.39], ['Tomate', ]]


peoples = {}
funcionario = []

# for p in range(3):
#     peoples['nome'] = input('Nome do funcionario: ')
#     peoples['profissao'] = input('Profissao do funcionario: ')
#     peoples['setor'] = input('Setor do funcionario: ')
#     funcionario.append(peoples.copy())

_links = ['home','profissões', 'contato', 'funcionarios', 'pagamentos', 'sair']
_escolha = ''
_isActive = False

if _links:
    _isActive = True
else:
    _isActive = False

while _isActive:
    print('='*10)
    for items in _links:
        print(items)
    print('='*10)
    _escolha = input('Sua opção: ')
    if _escolha == 'sair':
        print('Saindo do sistema...')
        _isActive = False
        break

def funcionarios(nome):
    print(f'Nome: {nome}')
