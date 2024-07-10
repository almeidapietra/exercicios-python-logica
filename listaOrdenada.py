#Faça um programa que leia três números e, em seguida, exiba-os em ordem crescente.

numero_1 = int(input('Informe o primeiro número '))
numero_2 = int(input('Informe o segundo número '))
numero_3 = int(input('Informe o terceiro número '))
 
lista = [ numero_1, numero_2, numero_3]
lista.sort()
print(lista)