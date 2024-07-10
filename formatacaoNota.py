# Elabore um programa que lê o nome e a nota de um aluno, depois exibe esses dados, mas com a nota formatada para exibir apenas uma casa decimal.

nome = input('Digite o nome do aluno ')
nota = float(input('Digite a nota do aluno '))
notaFormatada = "{:.1f}".format(nota)

print('Aluno: ' + nome + "\n Nota: " + notaFormatada)