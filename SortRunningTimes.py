import random
from time import time
import numpy as np

n = 10
A = [i for i in range(n)]
random.shuffle(A)

def insetionSort(L):
    for i in range(1, n):
        key = L[i]
        j = i - 1
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]
            j = j - 1
        L[j + 1] = key
    return L

def merge(A, B):
    out = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            j += 1
    while i < len(A):
        out.append(A[i])
        i += 1
    while j < len(B):
        out.append(B[j])
        j += 1
    return out

def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L) // 2
        Left = mergeSort(L[:mid])
        Right = mergeSort(L[mid:])
        return merge(Left, Right)


# print(insetionSort(A))
# sorted_A = mergeSort(A)
# print(sorted_A)
# print('After merge sorting: ')
# print(A)

def bubbleSort(L):
    index_length = len(L) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if L[i] > L[i+1]:
                sorted = False
                L[i], L[i + 1] = L[i + 1], L[i]
    return L

def rand_array(n):
    A = [i for i in range(n)]
    random.shuffle(A)
    return A

n_values = np.arange(100, 5100, 100)
times_insertion1 = []
times_insertion2 = []
times_insertion3 = []

for n in n_values:
    A = rand_array(n)

    t1 = time()
    B = insetionSort(A)
    t2 = time()

    mtime1 = (t2-t1) * 1000
    times_insertion1.append(mtime1)

for n in n_values:
    A = rand_array(n)

    t3 = time()
    C = mergeSort(A)
    t4 = time()

    mtime2 = (t4-t3) * 1000
    times_insertion2.append(mtime2)

for n in n_values:
    A = rand_array(n)

    t5 = time()
    D = bubbleSort(A)
    t6 = time()

    mtime3 = (t6-t5) * 1000
    times_insertion3.append(mtime3)

print(f"{'N':<10}\t{'Insertion Sort':<20}\t{'Merge Sort':<20}\t{'Bubble Sort':<20}")

for i, n in enumerate(n_values):
    print(f"{n:<10}\t{times_insertion1[i]:<20.1f}\t{times_insertion2[i]:<20.1f}\t{times_insertion3[i]:<20.1f}\n")