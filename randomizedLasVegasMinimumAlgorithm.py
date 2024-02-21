import time
import random


def findMinimum(arr):
    if not arr:
        raise ValueError("Array is empty")

    min_element = arr[0]
    for element in arr[1:]:  # If a smaller element is found, update min_element
        if element < min_element:
            min_element = element
    return min_element


def lasVegasFindMin(arr):
    iteration = 0
    while True:
        iteration += 1
        # Shuffle the array to introduce randomness
        random.shuffle(arr)

        # Attempy to find the minimum element
        try:
            start_time = time.time()  # Record the start time
            min_element = findMinimum(arr)
            end_time = time.time()  # Record the end time
            run_time = end_time - start_time  # Calculate the runtime
            print(f"Iteration {iteration}: Minimum element found: {min_element}, Runtime:{run_time:.6f} seconds")
            return min_element
        except ValueError:
            # If the arrays is empty after shuffling, try again
            continue


# Example array
arr = [5, 9, 2, 6, 3, 8]
minimum = lasVegasFindMin(arr)
print("Final minimum element found: ", minimum)
