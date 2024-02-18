import random
def partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Randomly select the pivot element/index
    pivot = arr[pivot_index]
    # Move the pivot to the end
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomizedQuickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        randomizedQuickSort(arr, low, pivot_index - 1)
        randomizedQuickSort(arr, pivot_index + 1, high)


# Example
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
randomizedQuickSort(arr, 0, len(arr) - 1)
print("Sorted Array: ", arr)
