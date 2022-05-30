#ENTRADA
total_conta = float(input('Digite o valor total da conta: ').replace(',' , '.'))
numero_pessoas = int(input('Digite o número de pessoas que irão dividir a conta: '))
gorjeta = int(input('Digite a % que deseja dar de gorjeta: '))

#PROCESSAMENTO
valor_dividido = float(total_conta / numero_pessoas)
valor_gorjeta = float((gorjeta / 100) * total_conta)
valor_final = round(float(valor_dividido + valor_gorjeta), 2)
total_conta = str(total_conta).replace('.' , ',')
valor_final = str(valor_final).replace('.' , ',')

#SAÍDA
print(f'O valor total da conta é {total_conta} e cada uma das {numero_pessoas} pessoas deve pagar {valor_final}.')