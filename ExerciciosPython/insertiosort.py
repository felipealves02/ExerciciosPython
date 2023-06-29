def insertionSort(lista):
    for i in range(1, len(lista)):
        valorcorreto = lista[i]
        posiçao = i

        while posiçao > 0 and lista[posiçao-1]>valorcorreto:
            lista[posiçao] =lista[posiçao-1] 
            posiçao = posiçao-1
        lista[posiçao] = valorcorreto

lista = [54,23,10,17,55,20,32]
insertionSort(lista)
print(lista)