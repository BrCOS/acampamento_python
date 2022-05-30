palavra_secreta = 'Suco'

print('Dica: ')
print('''É bom para a saúde
líquido e aguado!''')

palavra = input('Digite a palavra secreta: ').capitalize() #Deixa a primeira letra da palavra entrada maiúscula
print(palavra == palavra_secreta)