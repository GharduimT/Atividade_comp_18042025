'''
Desenvolva um algorítimo que apresente: o Valor adequado, e inadequado de temperatura para a operação segura de sistema;

> O usuário precisa inserir o valor da temperatura aferido no sistema.
> De acordo com esse valor informar se é seguro seguir com a operação ou se é necessário solicitar manutenção do mesmo.

** até 15ºC (faixa segura)
** de 15ºC a 25ºC (manutenção)
** maior que 25ºC (desligar imediatamente)
'''
#Coleta de dados
print('\n Vamos avaliar a temperatura do sistema. \n') 
temp_aferida = float(input('Usuário, para mantermos o bom funcionamento do sistema, informe o valor da temperatura aferida aqui: '))

temp_limite = 15
temp_critica = 25
ok = ('Sistema operando em temperatura adequada, obrigado!')
manut = ('Realize a manutenção preventiva!')
desligue = ('Desligue o sistema imediatamente!')
#  processamento

if temp_aferida <= temp_limite:
    print (ok)
elif temp_limite < temp_aferida <= temp_critica:
    print(manut)
else:
    print (desligue)