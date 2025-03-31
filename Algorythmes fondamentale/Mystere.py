A = [12,25,42,3,4,13]


def mystere(arr, low, high):
    pivot = arr[0]
    low = low-1
    high = high + 1

    while 1:
        low = low + 1
        high = high - 1

        while arr[low] < pivot:
            low = low + 1
        while arr[high] > pivot:
            high = high - 1
        if low > high :
            return high



idx = mystere(A, 0,len(A)-1)