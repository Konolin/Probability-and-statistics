import numpy as np
from scipy.stats import binom

prob_no_defect = 0.80
prob_light_defect = 0.15
prob_big_defect = 0.05

# a) Man simuliere N=100 mögliche Werte der ZG X.
num_simulations = 100
num_products = 100
big_defects = []
for _ in range(num_simulations):
    simulated_data = np.random.choice(["no_defect", "light_defect", "big_defect"], size=num_products, replace=True,
                                      p=[prob_no_defect, prob_light_defect, prob_big_defect])
    big_defects.append(np.sum(simulated_data == "big_defect"))
print(f"{num_simulations} simulations and their number of big_defects priducts:\n", big_defects)

# b) Welches ist die mittlere Anzahl M der Waren mit großen Fehlern (anhand der simulierten Daten)?
num_big_defect = 0
for _ in range(num_simulations):
    simulated_data = np.random.choice(["no_defect", "light_defect", "big_defect"], size=num_products, replace=True,
                                      p=[prob_no_defect, prob_light_defect, prob_big_defect])
    num_big_defect += np.sum(simulated_data == "big_defect")
print("Average number of big defects: ", num_big_defect / num_simulations)

# c) Wie groß ist die theoretische Wahrscheinlichkeit, dass von den nächsten hergestellten 100 Exemplaren dieser Ware
# 1) höchstens 3; 2) genau 10; 3) mindestens 4 große Fehler besitzen?
print(f"Theoretical probability max 3: {binom.cdf(3, num_products, prob_big_defect):.2f}")
print(f"Theoretical probability exactly 10: {binom.pmf(10, num_products, prob_big_defect):.2f}")
print(f"Theoretical probability min 4: {1 - binom.cdf(3, num_products, prob_big_defect):.2f}")
