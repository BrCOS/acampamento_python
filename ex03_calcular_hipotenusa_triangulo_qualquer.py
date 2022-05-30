#ENTRADA
cateto_adjacente = input('Digite o cateto adjacente: ').replace(',' , '.')
cateto_oposto = input('Digite o cateto oposto ').replace(',' , '.')

#PROCESSAMENTO
hipotenusa = round((float(cateto_adjacente) ** 2 + float(cateto_oposto) ** 2) ** (1/2),2)
hipotenusa = str(hipotenusa).replace(',' , '.')

#SAÍDA
print(f'A hipotenusa é {hipotenusa}')