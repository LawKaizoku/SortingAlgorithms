# QuickSort em Python

# array[] -> Array que será ordenado
# menorNum -> menor posição
# maiorNum -> maior posição
def part(array, menorNum, maiorNum):
    i = (menorNum - 1)  # posição do menor elemento
    pivor = array[maiorNum]  # Escolhemos o último como pivor

    for j in range(menorNum, maiorNum):

        # Se o atual elemento é menor ou igual ao pivor
        if array[j] <= pivor:
            # aumentar posição do menor elemento
            i = i + 1
            array[i], array[j] = array[j], array[i]
            print(array)

    array[i + 1], array[maiorNum] = array[maiorNum], array[i + 1]
    return (i + 1)


# Função Quick
def quickSort(array, menorNum, maiorNum):
    if len(array) == 1: # se o array for de tamanho 1, ele retorna o array, pois só haverá um elemento
        return array
    if menorNum < maiorNum:
        # aux está fazendo o papel de pivor
        aux = part(array, menorNum, maiorNum)
        quickSort(array, menorNum, aux - 1)
        quickSort(array, aux + 1, maiorNum)


# Teste de ordenação
array = [6,5,2,4,3]
n = len(array)
quickSort(array, 0, n - 1)
print(array)


# Código feito por LawKaizoku
