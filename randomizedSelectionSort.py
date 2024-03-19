import random


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # Find the minimum element in the unsorted path of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]


def randomized_selection_sort(arr):
    random.shuffle(arr)  # Shuffle the array randomly
    selection_sort(arr)  # use selection sort to sort the shuffled array


# Example unsorted array
arr = [3, 6, 1, 8, 2, 5, 7, 4]
print("Original array:", arr)
randomized_selection_sort(arr)
print("Sorted array:", arr)
