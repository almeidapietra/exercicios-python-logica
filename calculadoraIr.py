#Elabore um programa que leia o salário mensal de uma pessoa, realize o cálculo do imposto de renda e, por fim, informe se a pessoa deve declarar ou não o imposto de renda. Assuma que será obrigada a apresentar a declaração anual a pessoa que receber rendimentos tributáveis, sujeitos ao ajuste na declaração, cuja soma foi superior a R$ 28.559,70.

salario = float(input('Informe o seu salário '))
if salario >= 28599.70 :
    ir = (salario * 27.5) / 100
    print(f'Necessário declarar o IR, no valor de R$ {ir}')
else:
    print('Desnecessário declarar IR')