#ENTRADA
velocidade_ms = input('Digite o valor da velocidade em m/s: ').replace(',' , '.')

#PROCESSAMENTO
velocidade_kmh = round(3.6 * float(velocidade_ms), 2)

#SAÍDA
print(f'O resultado de {velocidade_ms} m/s em KM/h é: {velocidade_kmh}')