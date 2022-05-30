#Programa que o usuário informa 2 números e ele retorna a parte inteira da divisão (na saída usar número int)
#ENTRADA
num1 = float(input('Digite o primeiro número: ')) #Entrada de um número qualquer
num2 = float(input('Digite o segundo número: '))  #Entrada de um número qualquer

#PROCESSAMENTO
divisao_int = int(num1 // num2) #O "//" pega a parte inteira da divisão

#SAÍDA 
print(f'A parte inteira da divisão entre {num1} e {num2} é {divisao_int}')