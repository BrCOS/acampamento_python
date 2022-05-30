#ENTRADA
velocidade_kmh = input('Digite o valor em KMH: ').replace(',' , '.')

#PROCESSAMENTO
velocidade_ms = round(float(velocidade_kmh) / (3.6), 2)

#SAÍDA
print(f'O valor de {velocidade_kmh}km/h em m/s é {velocidade_ms}')