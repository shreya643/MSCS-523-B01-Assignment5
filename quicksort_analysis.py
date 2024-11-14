import random
import time

# Deterministic Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Randomized Quicksort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)


def generate_array(size, dist_type):
    if dist_type == 'random':
        return [random.randint(0, 1000) for _ in range(size)]
    elif dist_type == 'sorted':
        return list(range(size))
    elif dist_type == 'reverse_sorted':
        return list(range(size, 0, -1))

def empirical_comparison(sizes, distributions):
    for size in sizes:
        for dist_type in distributions:
            arr = generate_array(size, dist_type)

            # Test deterministic Quicksort
            arr_copy = arr.copy()
            start_time = time.time()
            quicksort(arr_copy)
            deterministic_time = time.time() - start_time

            # Test randomized Quicksort
            arr_copy = arr.copy()
            start_time = time.time()
            randomized_quicksort(arr_copy)
            randomized_time = time.time() - start_time

            
            print(f"Size: {size}, Distribution: {dist_type}, "
                  f"Deterministic Time: {deterministic_time:.6f} seconds, "
                  f"Randomized Time: {randomized_time:.6f} seconds")



sizes = [100, 1000, 10000]
distributions = ['random', 'sorted', 'reverse_sorted']


results = empirical_comparison(sizes, distributions)
