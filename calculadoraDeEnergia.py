# Faça um programa que calcule a conta de energia elétrica, solicitando apenas o número de kW/h e levando em consideração:
#  a)     O preço do kW/h é R$ 0,56.
#  b)     O valor da Geração de energia é 41% do valor do consumo.
#  c)     O valor de imposto é de 22,52% do valor do consumo.
#  d)     Qual a “bandeira” (acréscimo a cada kWh consumido) tarifária está em vigor:
#                        I.         Amarela: R$ 0,015.
#                       II.         Bandeira vermelha - Patamar 1: R$ 0,040.
#                      III.         Bandeira vermelha - Patamar 2: R$ 0,060.
#  Informe o valor final da conta de Energia.


kw = int(input('Informe o número de KW/h do período  '))
valorConsumo = kw * 0.56
geracaoEnergia = valorConsumo * 0.41
imposto = 0.2252 * valorConsumo

bandeira = input('Qual a bandeira tarifária em vigor (amarela, vermelha_1 ou vermelha_2)? ').lower()

if bandeira == 'amarela' :
    tarifaBandeira = 0.015 * valorConsumo
elif bandeira == 'vermelha_1':
    tarifaBandeira = 0.040 * valorConsumo
elif bandeira == 'vermelha_2' :
    tarifaBandeira = 0.060 * valorConsumo
else:
    print('Bandeira tarifária inválida. Escolha entre amarela, vermelha_1 ou vermelha_2.')
    tarifaBandeira = 0

    
contaEnergia = valorConsumo + geracaoEnergia + imposto + tarifaBandeira
print(f'O valor da conta de energia é de R$ {contaEnergia:.2f}')