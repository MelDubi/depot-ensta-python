import math as m
import random as rd

def partition(A, idx_low, idx_high):
    # Hoare's algotithm, faster than Lomuto's
    # Does not guarantee where the pivot lands
    # All element before returned index will be lower or equal than pivot
    # Random pivot 
    pivot = A[rd.randrange(idx_low, idx_high)]
    idx_low -= 1
    idx_high += 1
    while True:
        idx_low += 1
        idx_high -=1
        
        while A[idx_low] < pivot:
            idx_low += 1
        while A[idx_high] > pivot:
            idx_high -= 1

        if idx_low >= idx_high:
            return idx_high
        
        A[idx_low], A[idx_high] = A[idx_high], A[idx_low]

def quickSort(arr, low, high):
    if (low < high):
 
        pi = partition(arr, low, high)
 
        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)
        
A = list(range(21))
rd.shuffle(A)
A[5] = A[-1]


print(A)
idx = quickSort(A, 0, len(A) - 1)
print(A)