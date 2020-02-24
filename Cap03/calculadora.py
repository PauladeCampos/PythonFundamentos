#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('\n\n******************** CALCULADORA PYTHON ********************\n\n')

print('Selecione uma das opções abaixo: \n')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

opcao = int(input('\nDigite sua opção (1/2/3/4): '))

if opcao == 1:
    num1 = int(input('\nDigite o primeiro número: '))
    num2 = int(input('\nDigite o segundo número: '))
    print('\n%s + %s = %s \n' %(num1,num2,num1+num2))

elif opcao == 2:
    num1 = int(input('\nDigite o primeiro número: '))
    num2 = int(input('\nDigite o segundo número: '))
    print('\n%s - %s = %s \n' %(num1,num2,num1-num2))

elif opcao == 3:
    num1 = int(input('\nDigite o primeiro número: '))
    num2 = int(input('\nDigite o segundo número: '))
    print('\n%s * %s = %s \n' %(num1,num2,num1*num2))

elif opcao == 4:
    num1 = int(input('\nDigite o primeiro número: '))
    num2 = int(input('\nDigite o segundo número: '))
    print('\n%s / %s = %s \n' %(num1,num2,num1//num2))

else:
    print('\n\nOpção inválida!!!\n\nTente novamente!!!')