import numpy as np

matB = np.random.randint(1, 100, (3, 3))
matA = np.random.randint(1, 100, (3, 3))

print(f"A = {matA}")
print(f"\nB = {matB}")
print(f"\nA . B = \n{matA * matB}")