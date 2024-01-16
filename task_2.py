def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        iterations += 1

        if mid_value < target:
            low = mid + 1
        elif mid_value > target:
            high = mid - 1
        else:
            return iterations, mid_value

    # If the target is not found, return the upper bound
    if high < 0:
        return iterations, arr[0]
    elif low >= len(arr):
        return iterations, arr[-1]
    else:
        return iterations, arr[low]

# Приклад використання:
sorted_array = [0.1, 0.5, 0.7, 1.2, 2.0, 3.5, 5.2, 8.0]
target_value = 2.3

iterations, upper_bound = binary_search(sorted_array, target_value)

print(f"Елемент {target_value} знайдений за {iterations} ітерацій. Верхня межа: {upper_bound}")
