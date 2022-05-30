#ENTRADA
temperatura_kelvin = input('Digite a temperatura em K: ').replace(',' , '.')#.replace utilizado para substituir algo, neste caso ('quro trocar este' , 'por este')

#PROCESSAMENTO
temperatura_celsius = round(float(temperatura_kelvin) + (-273.15) , 2)#round utilizado para arredondar, neste caso, até duas casas depois da vírgula
temperatura_celsius_br = str(temperatura_celsius).replace('.' , ',')#.replace utilizado para substituir algo, neste caso ('quro trocar este' , 'por este')

#SAÍDA
print(f'''{temperatura_kelvin}K em °C no padrão internacional é {temperatura_celsius}°C
E no padrão brasileiro é {temperatura_celsius_br}°C''')