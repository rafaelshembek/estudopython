import random


def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x
def vencedor(jogador1, jogador2):
    global v1, v2, empate
    if jogador1 == 1: #Pedra
        if jogador2 == 1: # Pedra
            empate += 1
        elif jogador2 == 2: #Papel
            v2 += 1
        elif jogador2 == 3: #Tesoura
            v1 += 1
    elif jogador1 == 2: #Papel
        if jogador2 == 1: # Pedra
            v1 += 1
        elif jogador2 == 2: #Papel
            empate += 1
        elif jogador2 == 3: #Tesoura
            v2 += 1
    elif jogador1 == 3:  # Tesoura
        if jogador2 == 1:  # Pedra
            v2 += 1
        elif jogador2 == 2:  # Papel
            v1 += 1
        elif jogador2 == 3:  # Tesoura
            empate += 1
    resultados = [v1, v2, empate]
    return  resultados

print('JOKENPO')
print('1 -- Pedra')
print('2 -- Papel')
print('3 -- Tesoura')
print('0 -- Ver o resultado')

jogadas = []
resultados = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha sua jogada ', 0, 3)
    if not j1:
        break
    j2 = random.randint(1,3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

for jogada in jogadas:
    for dados in jogada:
        print(f'Vitoria: {dados}', end=' ')
    print()

print(f'Numeros de vitorias do jogador 1: {resultados[0]}')
print(f'Numeros de vitorias do Computador: {resultados[1]}')
print(f'Numeros de empate: {resultados[2]}')