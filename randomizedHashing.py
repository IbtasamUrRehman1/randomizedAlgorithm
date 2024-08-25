import numpy as np
import matplotlib.pyplot as plt

class RandomizedHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.hash_function = lambda x: int((x * np.random.uniform()) % size)

    def insert(self, key):
        idx = self.hash_function(key)
        self.table[idx].append(key)

    def visualize(self):
        plt.figure(figsize=(8, 5))
        for idx, bucket in enumerate(self.table):
            plt.scatter([idx] * len(bucket), bucket, label=f'Bucket {idx}')
        plt.xlabel('Hash Table Index')
        plt.ylabel('Keys')
        plt.title('Randomized Hashing Visualization')
        plt.legend()
        plt.show()

    def print_table(self):
        for idx, bucket in enumerate(self.table):
            print(f"Bucket {idx}: {bucket}")

# Example Usage
keys = np.random.randint(1, 100, 20)
hash_table = RandomizedHashTable(size=10)
for key in keys:
    hash_table.insert(key)

hash_table.print_table()
hash_table.visualize()
