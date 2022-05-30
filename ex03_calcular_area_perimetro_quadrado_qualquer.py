#ENTRADA
from sys import float_repr_style


lado = input('Digite o lado do quadrado: ')

#PROCESSAMENTO

area = float(lado) ** 2
perimetro = 4 * float(lado)

#SAÍDA
print(f'''A área do quadrado é {area}
O perímetro é {perimetro}''')