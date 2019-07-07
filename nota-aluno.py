x = str(input('Ola bom dia! Qual seu nome: '))
print('Ola', x, 'vamos ver sus nota agora!')
n = int(input('digite sua nota para iniciar os calculos: '))

media = 6

if n >= 6:
    print('Parabens', x, 'voce foi aprovado direto')
elif n ==5:
    print('sinto muito', x, 'voce esta de recuperacao mas ainda nao foi reprovado')
else:
    print('segundo nosso sistema', x, 'voce foi reprovado direto')

print ('Obrigado', x, 'por utilizar nossos serviços BYE-BYE!')


