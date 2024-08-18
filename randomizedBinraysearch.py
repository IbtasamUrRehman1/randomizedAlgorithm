import random
import matplotlib.pyplot as plt

def randomized_binary_search(arr, target, low, high, steps):
    if low > high:
        return -1
    mid = random.randint(low, high)
    steps.append(mid)
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return randomized_binary_search(arr, target, low, mid - 1, steps)
    else:
        return randomized_binary_search(arr, target, mid + 1, high, steps)

def visualize_search(arr, target):
    steps = []
    index = randomized_binary_search(arr, target, 0, len(arr) - 1, steps)
    plt.plot(arr, 'bo-', label="Array Elements")
    plt.axhline(y=target, color='g', linestyle='--', label="Target")
    plt.scatter(steps, [arr[i] for i in steps], color='r', label="Search Path")
    plt.title(f'Randomized Binary Search - Target: {target}')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
    return index

# Example
arr = sorted([random.randint(1, 100) for _ in range(15)])
target = arr[random.randint(0, len(arr) - 1)]
result = visualize_search(arr, target)
print(f"Target {target} found at index {result}")
