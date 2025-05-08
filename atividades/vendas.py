'''funcionario = (input('Informe o nome do funcionário: '))
vendas = int(input('Informe quantas unidades ' + funcionario + ' vendeu no mês: ')) # pelo que encontrei o uso do +...+ é chamado concatenação e permitiu puxar o resultado da primeira variável na segunda

if vendas >= 100:
    print('Gestor, esse mês', funcionario, 'obteve um desempenho Excelente')
elif vendas >= 70:
    print('Gestor, esse mês', funcionario, 'obteve um desempenho Bom')
elif vendas >= 30:
    print('Gestor, esse mês', funcionario, 'obteve um desempenho Ok')
else:
    print('Gestor, esse mês', funcionario, 'obteve um desempenho Insuficiente')'''

''' No entanto se fizer com f-string é possivel fazer mais coisas e de maneira mais legível(apesar de ser menos intuitivo, na minha cabeça, deescrever kkkkk)'''

'''#guarda o nome
nome_vendedor = (input('Informe o nome do(a) funcionário(a): '))

#vai pedir o número de vendas
uniades_vendidas = int(input(f'Informe quantas unidades {nome_vendedor} vendeu no mês: '))

#parte lógica
if uniades_vendidas >= 100:
    print(f'Gestor, esse mês, {nome_vendedor} obteve um desempenho Excelente')
elif uniades_vendidas>= 70:
    print(f'Gestor, esse mês, {nome_vendedor} obteve um desempenho Bom')
elif uniades_vendidas >= 30:
    print(f'Gestor, esse mês, {nome_vendedor} obteve um desempenho ok')
else:
    print(f'Gestor, esse mês, {nome_vendedor} obteve um desempenho Insuficiente')
#FIM DO PROGRAMAA   '''

''' E tem uma outra forma também usando f-string'''
nome_vendedor = input('Informe o nome do(a) funcionário(a): ')
unidades_vendidas = int(input(f'Informe quantas unidades {nome_vendedor} vendeu no mês: '))

#parte lógica / atenCAO para nao colocar acentuaCAO
if unidades_vendidas >= 100:
    classificacao ='EXCELENTE'
elif unidades_vendidas >= 70:
    classificacao ='BOM'
elif unidades_vendidas >= 30:
    classificacao ='OK'
else:
    classificacao ='INSUFICIENTE'
#Saida formatada (aqui como asvariáveisforam declaradas com f-string posso chama-las dentro da string a emforma de resultado "listado")
print(f'\n Este é o Relatório de Desempenho\n'
      f'O Vendedor: {nome_vendedor}\n'
      f'Vendeu: {unidades_vendidas} unidades no mês\n'
      f'Pelo volume de vendas sua Classificação no período é : {classificacao}')
#Mudançaspossíveis
    # 1)Na variavel do nome: print com Primeira Letra Maiúscula, pedir nome completo, Aceitar somente Caraceres usados para nome (com informe de erro e possibilidade de repetição p corrigir ou seguir como está ou cancelar a operação)
    # 2)Na variável número somente números inteiros(tipo de produtos? estoque?), com informe de erro e possibilidade de repetição p corrigir ou cancelar a operação.
    