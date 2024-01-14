import math
import random

success_prob = 0.85
simulations = 1000
misses = 0

for _ in range(simulations):
    attempts = random.choices([0, 1], [1 - success_prob, success_prob], k=3)
    if 0 in attempts:
        misses += 1

estimated_prob = misses / simulations
print("Estimated prob:", estimated_prob)

print(f"Theoretical : {1 - math.pow(0.85, 3):.2f}")
