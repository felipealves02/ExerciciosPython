ni = int(input('Digite o inicio do intervalo: '))
nf = int(input('Digite o fim do intervalo: '))
n = int(input('Digite um numero impar: '))
while n % 2 == 0:
    n = int(input('Digite um numero impar: '))
lista_primos = []
lista_pares = []
lista_divisor = []
for primo in range(ni, nf) + 1:
    if ni % 2 == 0:
