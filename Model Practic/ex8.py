# Seien n=4, p=0.25, X~Bino(n,p), Y=X^2 + 1. Man simuliere 1000 Werte für Y. Man erstelle das Histogramm
# der absoluten Häufigkeiten für Y. Man schätze P(Y>5). Man vergleiche die geschätzte Wahrscheinlichkeit mit der
# theoretischen Wahrscheinlichkeit.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 4
p = 0.25
sims = 1000
y = np.random.binomial(n, p, sims) ** 2 + 1

plt.hist(y, bins=range(min(y), max(y) + 1), edgecolor='black')
plt.show()

print(f"P(y > 5): {np.sum(y > 5) / sims}")
print(f"Theoretical: {1 - binom.cdf(5, n**2, p):.2f}")
