import os.path
from enum import Enum

# BACKEND DO PROGRAMA

def inicial():
    print(f'===> Menu')
def contato():
    print(f'===> Contatos')
def contas_a_pagar():
    print(f'===> Contas a Pagar')
def pagamento():
    print(f'===> Pagamentos')
def calculadoraIdade():
    nacimento = int(input('Entre com o ano de nacimento: '))
    yearAtual = int(input('Entre com o ano atual: '))
    print(yearAtual - nacimento)
def cadastroDeFuncionarios():

    if (os.path.exists('funcionarios.txt')):#Verificar se existe o arquivo par agravar os dados

        print('='*5+'MENU'+'='*5)
        _mostra = input('[m] - mostra\n[n] - novo cadastro \n[s] - para sair:\n[v] - voltar ao menu ')
        match (_mostra.upper()):

            case 'M':
                with open('funcionarios.txt', 'r') as _funcionarios: # ele vai mostra os dados que tem no arquivo
                    print(f'=' * 5)
                    for _linhas in _funcionarios:
                        print(f'\tFuncionario: {_linhas.strip()}') #mostra os dados na tela
                    print(f'=' * 5)
            case 'N':
                with open('funcionarios.txt', 'a') as _novosfuncionarios:
                    text = input('Nome do funcionario: ')
                    _novosfuncionarios.writelines(f'\n{text}')
            case 'V':
                menuPrograma()
    else: # caso não existe ele criar e escreve os dados no arquivo
        with open('funcionarios.txt', 'a') as _novosfuncionarios:
            text = input('Nome do funcionario: ')
            _novosfuncionarios.writelines(f'{text}\n')
def menuPrograma():
    print('1 - Home')
    print('2 - Contato')
    print('3 - Contas a Pagar')
    print('4 - Pagamentos')
    print('5 - Calcular Idade')
    print('6 - Cadastro de Funcionarios')
    print('7 - Sair do Programa')


class Opcoes(Enum):
    MENU = 1
    CONTATO = 2
    CONTAS_A_PAGAR = 3
    PAGAMENTO = 4
    CALCULAR_IDADE = 5
    CADASTRO_DE_FUNCIONARIOS = 6
    SAIR = 7


# FRONT END DO PROGRAMA
while True:
    menuPrograma()
    _menu = int(input('Entre com o numero da escolha: '))
    try:
        _opcoes = Opcoes(_menu)
        match _opcoes:
            case Opcoes.MENU:
                inicial()
            case Opcoes.CONTATO:
                contato()
            case Opcoes.CONTAS_A_PAGAR:
                contas_a_pagar()
            case Opcoes.PAGAMENTO:
                pagamento()
            case Opcoes.CALCULAR_IDADE:
                calculadoraIdade()
            case Opcoes.CADASTRO_DE_FUNCIONARIOS:
                cadastroDeFuncionarios()
            case Opcoes.SAIR:
                print('Programa encerrado...')
                break
    except ValueError:
        print('Opção inválida, por favor escolha novamente.')
