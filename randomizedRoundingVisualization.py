import random
import matplotlib.pyplot as plt


def randomizedRounding(weights, capacity):
    n = len(weights)
    solution = [0] * n
    total_weight = 0

    # Calculate fractional values
    fractions = [(weights[i], i) for i in range(n)]
    fractions.sort(key=lambda x: x[0] / capacity, reverse=True)

    # Perform randomized rounding and calculate total weight
    for weight, index in fractions:
        if random.random() < weight / capacity:
            solution[index] = 1
            total_weight += weights[index]

    return solution, total_weight, fractions


def visualizeRounding(weights, capacity):
    solution, total_weight, fractions = randomizedRounding(weights, capacity)

    # Prepare data for visualization
    items = [str(i + 1) for i in range(len(weights))]
    fractional_values = [weight / capacity for weight, _ in fractions]
    rounded_items = [1 if solution[i] == 1 else 0 for _, i in fractions]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(items, fractional_values, color='skyblue', label='Fractional Values')
    plt.bar(items, rounded_items, color='orange', label='Rounded Up', alpha=0.5)
    plt.xlabel('Items')
    plt.ylabel('Fractional Values / Rounded Up')
    plt.legend()
    plt.title('Randomized Rounding')
    plt.show()

# Example
weights = [2,3,4,5]
capacity = 7
visualizeRounding(weights, capacity)

