import numpy as np
import random
print("DoDoo shark was here")

simulation = 1000
spins = 4
win = 1
probability = 1/4

def spin():
    return random.randint(1, 4) == 1 # zicem ca daca pica 1 ai castigat

sim_wins = [sum(spin() for _ in range(spins)) >= win for _ in range(simulation)]

est_prob = np.mean(sim_wins)

print(f"Simulated Wins: {est_prob}")

from scipy.stats import binom

winning_probability = 1 / 4  # The probability of winning in a single spin
total_spins = 4

theoretical_probabilities = []
for k in range(total_spins + 1):
    probability = binom.pmf(k, total_spins, winning_probability)
    theoretical_probabilities.append((k, probability))

for k, probability in theoretical_probabilities:
    print(f"P(X = {k}) = {probability:.4f}")

# probability = 1 - binom.pmf(1, total_spins, winning_probability)
# print(probability)
