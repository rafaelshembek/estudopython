print('+ Mais')
print('- Menus')
print('* Multiplicação')
print('/ Divisão')
print('Presione qualquer outra tecla para sair.')

_op = input('Qual operação deseja realizar? ')
_valorOne = int(input('Digite o primeiro valor. '))
_valorTow = int(input('Digite o segundo valor. '))

if(_op == '+'):
    _result = _valorOne + _valorTow
    print(f'Resultado: {_valorOne} + {_valorTow} = {_result}')
elif(_op == '-'):
    _result = _valorOne - _valorTow
    print(f'Resultado: {_valorOne} - {_valorTow} = {_result}')
elif(_op == '*'):
    _result = _valorOne * _valorTow
    print(f'Resultado: {_valorOne} * {_valorTow} = {_result}')
elif(_op == '/'):
    _result = _valorOne / _valorTow
    print(f'Resultado: {_valorOne} / {_valorTow} = {_result}')
else:
    print('Encerrando o programa...')