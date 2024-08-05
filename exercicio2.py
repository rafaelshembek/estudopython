km = int(input('Digite o KM percorridos: '))
dias = int(input('Quantos dias foi percorridos? '))
valor_diaria = 60
valor_km_rodado = 0.15
preco_apagar = valor_diaria * dias +  valor_km_rodado * km

print(f'km rodado foram {km} quantidades de dias {dias}')
print(f'Valor a ser pago: {preco_apagar}')