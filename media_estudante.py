'''Dadas as 4 notas de um estudante, calcular sua média:  
Média maior que 7, emitir mensagem de aprovado;  
Média entre 5 e 7, emitir mensagem, que o estudante está em recuperação;  
Média abaixo de 5, emitir mensagem de reprovação. '''
#valor das variáeis são guardados
# try:
#     nota_1 = float(input(f'Informe quanto o aluno tirou na PROVA: '))
# except ValueError:
#     print('Erro: Digite apenas NÚMEROS!')
    
# #calcula a media da nota
# soma = nota_1 + nota_2 + nota_3 + nota_4
# media = soma/4

# #processamento

# if media >=7:
#     print(f'O aluno foi aprovado, sua média foi:{media}')
# # elif 5 > media =< 7
# #     print(f'O aluno está em recuperação, sua média foi:{media}')

# notas = []
# for i in range(4):
#     while True:
#         try:
#             nota = float(input(f'Digite a {i+1}ª nota: '))
#             notas.append(nota)
#             break
#         except:
#             print('Somente números serão aceitos!')
# media = sum(notas) / 4
# if media > 7:
#     print(f'Aprovado! Media: {media:.1f}')
# elif media >= 5:
#     print(f'Recuperação. Média: {media:.1f}')
# else:
#     print(f'Reprovado. Média: {media:.1f}')

#essa solução simplifica demais o código
notas = [float(input(f"Nota {i+1}:"))for i in range(4)]
media = sum(notas) / 4
print("Aprovado!"if media > 7 else "Recupração" if media >= 5 else "Reprovado!")