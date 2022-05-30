#ENTRADA
temperatura_celsius = input('Digite a temperatura em °C: ').replace(',' , '.')#.replace utilizado para substituir algo, neste caso ('quro trocar este' , 'por este')

#PROCESSAMENTO
temperatura_kelvin = round(273.15 + float(temperatura_celsius), 2)#round utilizado para arredondar, neste caso, até duas casas depois da vírgula
temperatura_kelvin_br = str(temperatura_kelvin).replace('.' , ',')

#SAÍDA

print(f'''No padrão internacional {temperatura_celsius}°C em Kelvin é {temperatura_kelvin}K
E no padrão brasileiro é {temperatura_kelvin_br}K''')