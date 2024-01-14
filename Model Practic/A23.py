# In einer Lostrommel sind 10 Gewinnlose und 30 Nieten. Wie groß ist die Wahrscheinlichkeit, man bei dreimaligem Ziehen
# a) mindestens ein Gewinnlos zieht? b) nur Nieten zieht?
# Welche ist die theoretische Wahrscheinlichkeitsverteilung der Zufallsgröße X: Anzahl der Gewinnlose beim dreimaligen
# Ziehen?

import math

# Total number of items in the drum
total_items = 40
# Number of winning items in the drum
winning_items = 10
# Number of draws
num_draws = 3

# Calculate the probability of getting at least one winning item
prob_at_least_one_win = 1 - (math.comb(30, 3) / math.comb(40, 3))

# Calculate the probability of getting all non-winning items (only Nieten)
prob_all_losers = (math.comb(30, 3) / math.comb(40, 3))

print("a) Probability of getting at least one Gewinnlos:", prob_at_least_one_win)
print("b) Probability of getting only Nieten (non-winning items):", prob_all_losers)

# Theoretical probability distribution of X (number of Gewinnlose in 3 draws)
theoretical_distribution = []
for k in range(4):  # Possible values of X (0, 1, 2, 3)
    prob = (math.comb(10, k) * math.comb(30, 3 - k)) / math.comb(40, 3)
    theoretical_distribution.append((k, prob))

print("c) Theoretical probability distribution of X:")
for k, probability in theoretical_distribution:
    print(f"P(X = {k}) = {probability:.4f}")
