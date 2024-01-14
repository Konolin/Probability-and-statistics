import numpy as np
from scipy.stats import norm

durchschnitt = 60
standardabweichung = 5
simulations = 1000
niederschlagsmenge = 55

x = np.random.normal(durchschnitt, standardabweichung, simulations)

estimated_prob = np.mean(x > niederschlagsmenge)

theoretical_prob = 1 - norm.cdf(niederschlagsmenge, durchschnitt, standardabweichung)

print(f"Estimated: {estimated_prob}")
print(f"Theoretical: {theoretical_prob}")
