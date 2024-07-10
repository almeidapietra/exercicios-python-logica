# Quatro times estão disputando as semifinais de um campeonato de futebol. Leia os gols que cada time marcou em suas partidas e informe qual time saiu vencedor. Em caso de empate em uma das partidas, leia o número de pênaltis cobrados corretamente (valores entre 0 e 5) para cada time. Supondo que haverá dois times vencedores das partidas, exiba-os. Exemplo de mensagem final: “Os times A e B estão na grande final!”.

timeA = 'Time A'
timeB = 'Time B'
timeC = 'Time C'
timeD = 'Time D'


golsTimeA_semifinal1 = int(input(f'Informe os gols do {timeA} na semifinal 1: '))
golsTimeB_semifinal1 = int(input(f'Informe os gols do {timeB} na semifinal 1: '))


if golsTimeA_semifinal1 > golsTimeB_semifinal1:
    vencedor_semifinal1 = timeA
    print(f'O {timeA} venceu a semifinal 1!')
elif golsTimeB_semifinal1 > golsTimeA_semifinal1:
    vencedor_semifinal1 = timeB
    print(f'O {timeB} venceu a semifinal 1!')
else:
    
    penaltisTimeA = int(input(f'Número de pênaltis convertidos pelo {timeA}: '))
    penaltisTimeB = int(input(f'Número de pênaltis convertidos pelo {timeB}: '))
    
    if penaltisTimeA > penaltisTimeB:
        vencedor_semifinal1 = timeA
        print(f'O {timeA} venceu a semifinal 1 nos pênaltis!')
    elif penaltisTimeB > penaltisTimeA:
        vencedor_semifinal1 = timeB
        print(f'O {timeB} venceu a semifinal 1 nos pênaltis!')
    else:
        print('Número de pênaltis convertidos iguais. Considere uma regra para desempate.')


golsTimeC_semifinal2 = int(input(f'Informe os gols do {timeC} na semifinal 2: '))
golsTimeD_semifinal2 = int(input(f'Informe os gols do {timeD} na semifinal 2: '))


if golsTimeC_semifinal2 > golsTimeD_semifinal2:
    vencedor_semifinal2 = timeC
    print(f'O {timeC} venceu a semifinal 2!')
elif golsTimeD_semifinal2 > golsTimeC_semifinal2:
    vencedor_semifinal2 = timeD
    print(f'O {timeD} venceu a semifinal 2!')
else:
    
    penaltisTimeC = int(input(f'Número de pênaltis convertidos pelo {timeC}: '))
    penaltisTimeD = int(input(f'Número de pênaltis convertidos pelo {timeD}: '))
    
    if penaltisTimeC > penaltisTimeD:
        vencedor_semifinal2 = timeC
        print(f'O {timeC} venceu a semifinal 2 nos pênaltis!')
    elif penaltisTimeD > penaltisTimeC:
        vencedor_semifinal2 = timeD
        print(f'O {timeD} venceu a semifinal 2 nos pênaltis!')
    else:
        print('Número de pênaltis convertidos iguais. Considere uma regra para desempate.')


print(f'Os times {vencedor_semifinal1} e {vencedor_semifinal2} estão na grande final!')
