print('Digite uma mensagem que irei repetir para você?')
print('Para encerrar escreva "sair".')
while True:
    _text = input('')
    print(f'{_text}')
    if _text == 'sair':
        break
print('Encerrando o programa....')