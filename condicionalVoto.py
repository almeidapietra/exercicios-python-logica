# Dê um exemplo de uso da estrutura condicional aninhada (if, elif e else):

idade = int(input('Informe a sua idade  '))

if  70 >= idade >= 18:
   print('Voto obrigatório')
elif 18 > idade >= 16  or idade > 70 :
    print('Voto facultativo')
else:
    print('Não pode votar')