###########################################################################
# Projeto de Estrutura de Dados II
# Algoritmos de Ordenação / Busca Binária e Sequêncial
#
# Equipe: Eduardo Buba - Mateus Maciel - Luiz Roberto.
###########################################################################
# Relação de Algoritmos a Serem Implementados:
# Simples:
#   * Insertion Sort;
#   * Selection Sort;
#   * Bubble Sort.
# Complexos:
#   * Odd-Even Sort;
#   * Intro Sort;
#   * Cycle Sort.
###########################################################################
# Imports
import time
import datetime
import math  # intro Sort
from heapq import heappush, heappop  # Intro Sort
###########################################################################


# ================================================================================================== #
# Abaixo seguem os métodos de todos os algoritmos.
# ================================================================================================== #


###########################################################################
# Insertion Sort
def insertionsort(f):
    global trc, cmp
    trc = cmp = 0
    for i in range(1, len(f)):
        key = f[i]
        j = i - 1
        cmp += 2
        while j >= 0 and key < f[j]:
            trc += 1
            f[j + 1] = f[j]
            j -= 1
            cmp += 2
        trc += 1
        f[j + 1] = key
    return f


###########################################################################


###########################################################################
# Selection Sort
def selectionsort(f):
    global trc, cmp
    trc = cmp = 0
    n = len(f)
    for i in range(n):
        key = i
        for j in range(i + 1, n):
            cmp += 1
            if f[key] > f[j]:
                key = j
        trc += 2
        f[i], f[key] = f[key], f[i]
    return f


###########################################################################


###########################################################################
# Bubble Sort
def bubblesort(f):
    global trc, cmp
    trc = cmp = 0
    n = len(f)
    for i in range(n):
        for j in range(0, n - i - 1):
            cmp += 1
            if f[j] > f[j + 1]:
                trc += 2
                f[j], f[j + 1] = f[j + 1], f[j]
    return f


###########################################################################


###########################################################################
# PigeonHole Sort
def pigeonhole_sort(f):
    global trc, cmp
    trc = cmp = 0  # Contadores de troca e comparação.
    n = len(f)
    x = f[0]
    for i in range(1, n):
        cmp += 1
        if f[i] < x:
            x = f[i]
    my_min = x
    x = f[0]
    for i in range(1, n):
        cmp += 1
        if f[i] > x:
            x = f[i]
    my_max = x

    size = my_max - my_min + 1  # Define numero de buracos.

    holes = [0] * size  # Cria o array de buracos.

    # Popula os buracos.
    for x in f:
        holes[x - my_min] += 1
        trc += 1

    # Coloca elementos de volta no array original.
    i = 0
    for count in range(size):
        cmp += 1
        while holes[count] > 0:
            trc += 1
            holes[count] -= 1
            trc += 1
            f[i] = count + my_min
            i += 1
    return f


###########################################################################


###########################################################################
# Tim Sort
minrun = 32


def inssort(arr, start, end):
    global trc, cmp
    for i in range(start + 1, end + 1):
        elem = arr[i]
        j = i - 1
        cmp += 2
        while j >= start and elem < arr[j]:
            trc += 1
            arr[j + 1] = arr[j]
            j -= 1
        trc += 1
        arr[j + 1] = elem
    return arr


def merge(arr, start, mid, end):
    global trc, cmp
    cmp += 1
    if mid == end:
        return arr
    first = arr[start:mid + 1]
    last = arr[mid + 1:end + 1]
    len1 = mid - start + 1
    len2 = end - mid
    ind1 = 0
    ind2 = 0
    ind = start

    cmp += 2
    while ind1 < len1 and ind2 < len2:
        cmp += 1
        if first[ind1] < last[ind2]:
            trc += 1
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            trc += 1
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1
    cmp += 1
    while ind1 < len1:
        trc += 1
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1
    cmp += 1
    while ind2 < len2:
        trc += 1
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1

    return arr


def timsort(arr):
    global trc, cmp
    trc = cmp = 0
    n = len(arr)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        trc += 1
        arr = inssort(arr, start, end)

    curr_size = minrun
    cmp += 1
    while curr_size < n:
        for start in range(0, n, curr_size * 2):
            mid = min(n - 1, start + curr_size - 1)
            end = min(n - 1, mid + curr_size)
            trc += 1
            arr = merge(arr, start, mid, end)
        curr_size *= 2
    return arr


###########################################################################


###########################################################################
# Intro Sort
def heapsort():
    global trc, cmp # variáveis globais de troca e comparações
    global arr # Array de valores
    h = [] # vetor vazio
    # construindo a pilha
    for value in arr:
        trc += 1
        heappush(h, value)
    arr = []
    # extraindo os elementos ordenados um por um
    trc += len(h)
    arr = arr + [heappop(h) for i in range(len(h))]


# A função principal para ordenar os dados utilizando o modelo de inserção como default
def insertionsort_intro(begin, end):
    global trc, cmp
    left = begin
    right = end
    # Traverse through 1 to len(arr)
    for i in range(left + 1, right + 1):
        key = arr[i]
        # Move elementos do array[0..i-1], que são
        # maiores que a chave, para uma posição adiante
        # da sua respectiva posição
        j = i - 1
        cmp += 2
        while j >= left and arr[j] > key:
            trc += 1
            arr[j + 1] = arr[j]
            j = j - 1
        trc += 1
        arr[j + 1] = key
   
# Essa função pega o ultimo elemento como pivot, aloca
# o elemento do pivot em sua posição correta no array
# ordenado, e aloca espaços para todos os elementos menores que o pivot
# na sua esquerda e todos os maiores a direita
# do pivot
def partition(low, high):
    global trc, cmp
    global arr
    # pivot
    pivot = arr[high]
    # índice do menor elemento
    i = low - 1
    for j in range(low, high):
        # Se o elemento correspondente é menor ou
        # igual ao pivot
        cmp += 1
        if arr[j] <= pivot:
            # incrementa o índice do menor elemento
            i = i + 1
            trc += 2
            (arr[i], arr[j]) = (arr[j], arr[i])
    trc += 2
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


# Função que mede a mediana
# de três elementos
# nos índices a,b,c
def medianofthree(a, b, d):
    global trc, cmp
    global arr
    A = arr[a]
    B = arr[b]
    C = arr[d]

    cmp += 2
    if A <= B <= C:
        return b
    cmp += 2
    if C <= B <= A:
        return b
    cmp += 2
    if B <= A <= C:
        return a
    cmp += 2
    if C <= A <= B:
        return a
    cmp += 2
    if B <= C <= A:
        return d
    cmp += 2
    if A <= C <= B:
        return d
    
# Função principal que implementa o Introsort
# low --> Início do índice
# high --> Fim do índice
# depthLimit --> nível de recursão
def introsortutil(begin, end, depthlimit):
    global trc, cmp
    global arr
    size = end - begin
    cmp += 1
    if size < 16:
        # se o tamanho dos dados for menor, método de inserção é chamado
        insertionsort_intro(begin, end)
        return
    cmp += 1
    if depthlimit == 0:
        # se a recursão limite for ultrapassada heap sort é chamada
        heapsort()
        return
    pivot = medianofthree(begin, begin + size // 2, end)
    trc += 2
    (arr[pivot], arr[end]) = (arr[end], arr[pivot])
    # partition_point é o índice de partição
    # arr[partition_point] está no lugar certo
    partition_point = partition(begin, end)
    # Separando os elementos ordenados antes e depois da partição
    introsortutil(begin, partition_point - 1, depthlimit - 1)
    introsortutil(partition_point + 1, end, depthlimit - 1)


# Função de utilidade para dar início ao método de ordenação
def introsortstart(begin, end):
    global trc, cmp
    trc = cmp = 0
    # inicializa a profundidade limite como 2 * log(length(data))
    depthlimit = 2 * math.log2(end - begin)
    introsortutil(begin, end, depthlimit)


def introsort():
    introsortstart(0, len(arr) - 1)


###########################################################################


# ================================================================================================== #
# Abaixo segue a 'main'.
# ================================================================================================== #


tipo = ['aleatorio', 'ordenado', 'repetido', 'reverso', 'semiOrdenado']
tam = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]

trc = cmp = 0

print('\nEsta aplicação implementa 6 tipos de algoritmos de ordenação em diferentes tamanhos de vetores.')
z = int(input('\n -> Deseja executar os simples (1) ou complexos (2)?'))

if z is 1:
    for j in range(0, len(tam)):
        for i in range(0, len(tipo)):
            arch = tipo[i] + str(tam[j]) + '.txt'
            with open(arch, 'r') as f:
                arr = f.readlines()
                f.close()
                for i in range(0, len(arr)):
                    arr[i] = int(arr[i])

                arr1 = arr.copy()
                arr2 = arr.copy()
                arr3 = arr.copy()

                print('\n-------------------------------------------')
                print('Início Ordenação: ')
                print(datetime.datetime.now())
                print('Sort: InsertionSort')
                print('Arquivo: ', arch)
                start = time.time()
                ord = insertionsort(arr1)
                end = time.time()
                print('Tempo: ', end - start)
                print('Comparações: ', cmp)
                print('Trocas: ', trc)
                time.sleep(0.5)

                print('\n-------------------------------------------')
                print('Início Ordenação: ')
                print(datetime.datetime.now())
                print('Sort: SelectionSort')
                print('Arquivo: ', arch)
                start = time.time()
                ord = selectionsort(arr2)
                end = time.time()
                print('Tempo: ', end - start)
                print('Comparações: ', cmp)
                print('Trocas: ', trc)
                time.sleep(0.5)

                print('\n-------------------------------------------')
                print('Início Ordenação: ')
                print(datetime.datetime.now())
                print('Sort: BubbleSort')
                print('Arquivo: ', arch)
                start = time.time()
                ords = bubblesort(arr3)
                end = time.time()
                print('Tempo: ', end - start)
                print('Comparações: ', cmp)
                print('Trocas: ', trc)
                time.sleep(0.5)


else:
    for j in range(0, len(tam)):
        for i in range(0, len(tipo)):
            arch = tipo[i] + str(tam[j]) + '.txt'
            with open(arch, 'r') as f:
                arr = f.readlines()
                f.close()
                for i in range(0, len(arr)):
                    arr[i] = int(arr[i])

                arr1 = arr.copy()
                arr2 = arr.copy()

                print('\n-------------------------------------------')
                print('Sort: PigeonSort')
                print('Arquivo: ', arch)
                start = time.time()
                ord = pigeonhole_sort(arr1)
                end = time.time()
                print('Tempo: ', end - start)
                print('Comparações: ', cmp)
                print('Trocas: ', trc)
                time.sleep(0.5)

                print('\n-------------------------------------------')
                print('Sort: TimSort')
                print('Arquivo: ', arch)
                start = time.time()
                ord = timsort(arr2)
                end = time.time()
                print('Tempo: ', end - start)
                print('Comparações: ', cmp)
                print('Trocas: ', trc)
                time.sleep(0.5)

                print('\n-------------------------------------------')
                print('Sort: Introsort')
                print('Arquivo: ', arch)
                start = time.time()
                introsort()
                ord = arr
                end = time.time()
                print('Tempo: ', end - start)
                print('Comparações: ', cmp)
                print('Trocas: ', trc)
                time.sleep(0.5)

                # print('Resultado: ')
                # for i in range(0, len(ord)):
                #    print(ord[i], end=' ')

# End
