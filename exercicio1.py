preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o percentual de desconto (0 a 100%): '))

desconto = preco * (percentual / 100)
final  = preco - desconto

print(f'O preço do produto {preco}. Desconto do produto {percentual}%')
print(f'O Valor calculado de desconto: {desconto}: valor final do produto: {final}')