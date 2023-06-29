primeiroTermo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
decimo = primeiroTermo + (10 -1)* razão
for i in range(primeiroTermo, decimo, razão):
    print(f'{i}', end=' , ')