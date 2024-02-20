import random


def randimizedQuickSelect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    if k < len(smaller):
        return randimizedQuickSelect(smaller, k)
    elif k < len(smaller) + len(equal):
        return pivot
    else:
        return randimizedQuickSelect(larger, k - len(smaller) - len(equal))

# Example
arr = [3,1,4,5,6,2]
k = 3
kth_smallest = randimizedQuickSelect(arr, k) # Adjusting for 0-based indexing
print(f"The {k}th smallest element is: ", kth_smallest)