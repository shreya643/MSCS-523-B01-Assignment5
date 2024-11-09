import random


def heapsort(arr):
    n = len(arr)
    

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


test_arrays = {
    'Random': [random.randint(0, 100) for _ in range(10)],
    'Sorted': sorted([random.randint(0, 100) for _ in range(10)]),
    'Reverse Sorted': sorted([random.randint(0, 100) for _ in range(10)], reverse=True)
}

def test_sorting_algorithms(test_arrays):
    results = {}

    for array_type, arr in test_arrays.items():
        results[array_type] = {}

        # Heapsort
        arr_copy = arr.copy()
        heapsort(arr_copy)
        results[array_type]['Heapsort'] = arr_copy

        # Quicksort
        arr_copy = arr.copy()
        results[array_type]['Quicksort'] = quicksort(arr_copy)

        # Mergesort
        arr_copy = arr.copy()
        mergesort(arr_copy)
        results[array_type]['Mergesort'] = arr_copy

    return results


test_results = test_sorting_algorithms(test_arrays)
for array_type, result in test_results.items():
    print(f"{array_type} Array:")
    for algorithm, sorted_array in result.items():
        print(f"  {algorithm}: {sorted_array}")
