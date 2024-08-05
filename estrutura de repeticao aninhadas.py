def soma(x=0,y=0,z=0):
    res = x + y + z
    return res

def valida_string(pergunta, min, max):
    try:
        _s1 = input(pergunta)
        _tam = len(_s1)
        while ((_tam < min) or (_tam > max)):
            _s1 = input(pergunta)
            _tam = len(_s1)
            break
        return _s1
    except ValueError:
        print('Opis, Erro em codigo...')

x = valida_string('Digite uma string: ', 10, 30)
print(f'Você digitou a string {x}. \n Dado válido. Encerrando o programa...')