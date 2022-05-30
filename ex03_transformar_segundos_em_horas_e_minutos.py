#ENTRADA
tempo_segundos = int(input('Digite o tempo em segundos: '))

#PROCESSAMENTO
tempo_horas = int(tempo_segundos // 3600)#Transforma os segundos em horas em valor inteiro

tempo_minutos = int(tempo_segundos % 3600) // 60 #Pega o resto da divisão entre segundos e 3600 e transforma em minutos

tempo_segundos_restantes = int(tempo_segundos % 60)#Pega o restante da divisão entre os segundos e 60

#SAÍDA
print(f'{tempo_segundos} segundos são {tempo_horas} horas, {tempo_minutos} minutos, {tempo_segundos_restantes} segundos')

#20399 -> 5 horas, 39 minutos e 59 segundos