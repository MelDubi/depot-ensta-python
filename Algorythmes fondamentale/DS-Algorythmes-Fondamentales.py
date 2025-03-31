
arr = [8, 56, 2, 5, 23, 216, 39, -5, 3, 8]

arr2 = [5, 4, 8, 25, 12, 42, 3, 42, 58]

def heapify(arr, n, heap_start):
    idx_left = 2*heap_start+1
    idx_right = 2*heap_start+2
    idx_largest = heap_start
    if idx_left < n and arr[idx_left] > arr[idx_largest]:
        idx_largest = idx_left
    if idx_right < n and arr[idx_right] > arr[idx_largest]:
        idx_largest = idx_right
    if idx_largest is not heap_start:
        change1 = arr[heap_start]
        change2 = arr[idx_largest]
        arr[heap_start] = change2
        arr[idx_largest] = change1
        heapify(arr, n, idx_largest)

def build_heap(arr):
    n = int(len(arr))
    for k in range(n//2, 0, -1):
        heapify(arr, n, k)


def heap_sort(arr):
    n = len(arr)
    build_heap(arr)
    for k in range(n):
        if arr[k] > arr[k+1]:
            max_arr = arr[k]
            min_arr = arr[0]
            arr[0] = max_arr
            arr[k] = min_arr
            heapify(arr, n-k-1, 1)


