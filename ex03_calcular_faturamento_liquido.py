#ENTRADA
faturamento_bruto = float(input('Digite o faturamento bruto: '))
taxa_imposto = float(input('Digite a porcentagem da taxa de imposto: '))
custos = float(input('Digite os custos: '))

#PROCESSAMENTO
impostos = faturamento_bruto * taxa_imposto / 100
faturamento_liquido = faturamento_bruto - impostos - custos 

#SAÍDA
print(f'O faturamento líquido foi de R${faturamento_liquido:.2f}')