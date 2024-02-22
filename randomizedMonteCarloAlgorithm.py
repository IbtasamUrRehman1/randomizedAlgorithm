import random
import matplotlib.pyplot as plt

def monteCarloPi(num_samples):
    inside_circle = 0
    inside_x, inside_y = [], []
    outside_x, outside_y = [], []

    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1,1)
        distance = x ** 2 + y ** 2

        if distance <= 1:
            inside_circle += 1
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)
    return 4 * inside_circle / num_samples, inside_x, inside_y, outside_x, outside_y


# Example
num_samples = 1000
estimated_pi, inside_x, inside_y, outside_x, outside_y = monteCarloPi(num_samples)
print("Estimated value of pi: ", estimated_pi)

#plotting
plt.figure(figsize=(8,8))
plt.scatter(inside_x, inside_y, color='blue', s=5, label='Inside Circle')
plt.scatter(outside_x, outside_y, color='red', s=5, label='Outside Circle')
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Monet Carlo Simulation for Estimating Pi')
plt.legend()
plt.show()












