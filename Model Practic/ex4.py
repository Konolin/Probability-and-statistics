import numpy as np

data = [309, 333, 309, 330, 325, 325, 325, 333, 314, 314, 330, 314, 314, 330]

print(f"a) Average lifetime of the bulbs: {np.mean(data):.2f}")
print(f"b) Empirical standard deviation: {np.std(data):.2f}")
print(f"c) Probability lifetime > 310: {np.sum(np.array(data) > 310) / len(data):.2f}")
