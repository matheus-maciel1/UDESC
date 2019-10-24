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
import math  # intro Sort
from heapq import heappush, heappop  # Intro Sort
# from functools import total_ordering  # Patience Sort
# from bisect import bisect_left  # Patience Sort
# from heapq import merge  # Patience Sort
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
        cmp = cmp + 2
        while j >= 0 and key < f[j]:
            f[j + 1] = f[j]
            trc += 1
            j -= 1
            cmp += 2
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
        f[i], f[key] = f[key], f[i]
        trc += 2
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
            if f[j] > f[j + 1]:
                f[j], f[j + 1] = f[j + 1], f[j]
    return f


###########################################################################


###########################################################################
# PigeonHole Sort
def pigeonhole_sort(f):
    global trc, cmp
    trc = cmp = 0
    # size of range of values in the list
    # (ie, number of pigeonholes we need)
    n = len(f)
    x = f[0]
    for i in range(1, n):
        if f[i] < x:
            x = f[i]
    my_min = x
    x = f[0]
    for i in range(1, n):
        if f[i] > x:
            x = f[i]
    my_max = x
    size = my_max - my_min + 1

    # our list of pigeonholes
    holes = [0] * size

    # Populate the pigeonholes.
    for x in f:
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1

    # Put the elements back into the array in order.
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            f[i] = count + my_min
            i += 1
    return f


###########################################################################


###########################################################################
# Patience Sort
'''
@total_ordering
class Pile(list):
    def __lt__(self, other): return self[-1] < other[-1]

    def __eq__(self, other): return self[-1] == other[-1]


def patience_sort(f):
    global trc, cmp
    trc = cmp = 0
    piles = []
    # sort into piles
    for x in f:
        new_pile = Pile([x])
        i = bisect_left(piles, new_pile)
        if i != len(piles):
            piles[i].append(x)
        else:
            piles.append(new_pile)

    # use a heap-based merge to merge piles efficiently
    f[:] = merge(*[reversed(pile) for pile in piles])
    return f

'''
###########################################################################
# Tim Sort
minrun = 32


def inssort(arr, start, end):
    for i in range(start + 1, end + 1):
        elem = arr[i]
        j = i - 1
        while j >= start and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr


def merge(arr, start, mid, end):
    if mid == end:
        return arr
    first = arr[start:mid + 1]
    last = arr[mid + 1:end + 1]
    len1 = mid - start + 1
    len2 = end - mid
    ind1 = 0
    ind2 = 0
    ind = start

    while ind1 < len1 and ind2 < len2:
        if first[ind1] < last[ind2]:
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1

    while ind1 < len1:
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1

    while ind2 < len2:
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1

    return arr


def timsort(arr):
    n = len(arr)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        arr = inssort(arr, start, end)

    curr_size = minrun
    while curr_size < n:
        for start in range(0, n, curr_size * 2):
            mid = min(n - 1, start + curr_size - 1)
            end = min(n - 1, mid + curr_size)
            arr = merge(arr, start, mid, end)
        curr_size *= 2
    return arr


###########################################################################


###########################################################################
# Intro Sort
def heapsort():
    global trc, cmp
    global arr
    h = []
    # building the heap
    for value in arr:
        heappush(h, value)
    arr = []
    # extracting the sorted elements one by one
    arr = arr + [heappop(h) for i in range(len(h))]


# The main function to sort the data using insertion sort algorithm
def insertionsort_intro(begin, end):
    global trc, cmp
    left = begin
    right = end
    # Traverse through 1 to len(arr)
    for i in range(left + 1, right + 1):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    # This function takes last element as pivot, places


# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(low, high):
    global trc, cmp
    global arr
    # pivot
    pivot = arr[high]
    # index of smaller element
    i = low - 1
    for j in range(low, high):
        # If the current element is smaller than or
        # equal to the pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


# The function to find the median
# of the three elements in
# in the index a, b, d
def medianofthree(a, b, d):
    global trc, cmp
    global arr
    A = arr[a]
    B = arr[b]
    C = arr[d]

    if A <= B <= C:
        return b
    if C <= B <= A:
        return b
    if B <= A <= C:
        return a
    if C <= A <= B:
        return a
    if B <= C <= A:
        return d
    if A <= C <= B:
        return d
    # The main function that implements Introsort


# low --> Starting index,
# high --> Ending index
# depthLimit --> recursion level
def introsortutil(begin, end, depthlimit):
    global trc, cmp
    global arr
    size = end - begin
    if size < 16:
        # if the data set is small, call insertion sort
        insertionsort_intro(begin, end)
        return
    if depthlimit == 0:
        # if the recursion limit is occurred call heap sort
        heapsort()
        return
    pivot = medianofthree(begin, begin + size // 2, end)
    (arr[pivot], arr[end]) = (arr[end], arr[pivot])
    # partition_point is partitioning index,
    # arr[partition_point] is now at right place
    partition_point = partition(begin, end)
    # Separately sort elements before partition and after partition
    introsortutil(begin, partition_point - 1, depthlimit - 1)
    introsortutil(partition_point + 1, end, depthlimit - 1)


# A utility function to begin the Introsort module
def introsortstart(begin, end):
    global trc, cmp
    trc = cmp = 0
    # initialise the depthlimit as 2 * log(length(data))
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

                print('\n-------------------------------------------')
                print('Sort: InsertionSort')
                print('Arquivo: ', arch)
                start = time.time()
                ord = insertionsort(arr)
                end = time.time()
                print('Tempo: ', end - start)
                print('Comparações: ', cmp)
                print('Trocas: ', trc)
                time.sleep(0.5)

                print('\n-------------------------------------------')
                print('Sort: SelectionSort')
                print('Arquivo: ', arch)
                start = time.time()
                ord = selectionsort(arr)
                end = time.time()
                print('Tempo: ', end - start)
                print('Comparações: ', cmp)
                print('Trocas: ', trc)
                time.sleep(0.5)

                print('\n-------------------------------------------')
                print('Sort: BubbleSort')
                print('Arquivo: ', arch)
                start = time.time()
                ord = bubblesort(arr)
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

                print('\n-------------------------------------------')
                print('Sort: PigeonSort')
                print('Arquivo: ', arch)
                start = time.time()
                ord = pigeonhole_sort(arr)
                end = time.time()
                print('Tempo: ', end - start)
                print('Comparações: ', cmp)
                print('Trocas: ', trc)
                time.sleep(0.5)

                print('\n-------------------------------------------')
                print('Sort: TimSort')
                print('Arquivo: ', arch)
                start = time.time()
                ord = timsort(arr)
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
