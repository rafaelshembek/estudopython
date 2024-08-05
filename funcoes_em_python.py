import random

# função para gerar nomes aleatorio
def RandomNomes(mylistNomes):
    _indice = random.randrange(len(mylistNomes))
    borda(_people[_indice])

# função para dar bordar em nomes
def borda(s1):
    tam = len(s1)
    if(tam):
        print('*','-'*tam,'*')
        print('|',s1,'|')
        print('*','-'*tam,'*')
def total_de_notas():
    _notas = int(input('Quantidade de notas: '))
    _nota = 1
    _result = 0
    while _nota <= _notas:
        _x = int(input(f'Entre com sua {_nota}ª nota: '))
        _nota += 1
        _result += _x
    print(f'Total da notas: {_result}')

borda('Nomes Aleatorios')
_people = ["Rafael Silva", "Laila Servero", "Bruna", "Ricardo"]
RandomNomes(_people)

# total_de_notas()