primeiro_numero = int(input('digite um numero: '))
operador = (input('escolha uma operação: '))
segundo_numero = int(input('digite o proximo numero: '))
if operador == '+':
    print(f'{primeiro_numero} + {segundo_numero}')
    print(f'{primeiro_numero} + {segundo_numero} = {primeiro_numero + segundo_numero} ')
elif operador == '-':
    print(f'{primeiro_numero} - {segundo_numero}')
    print(f'{primeiro_numero} - {segundo_numero} = {primeiro_numero - segundo_numero} ')
elif operador == '*':
    print(f'{primeiro_numero} * {segundo_numero}')
    print(f'{primeiro_numero} * {segundo_numero} = {primeiro_numero * segundo_numero} ')
elif operador == '/':
    print(f'{primeiro_numero} / {segundo_numero}')
    print(f'{primeiro_numero} / {segundo_numero} = {primeiro_numero / segundo_numero} ')
else:
    print('Digite uma operação valida')

 
