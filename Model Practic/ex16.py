# Sei X eine binomialverteile Zufallsgröße mit Parametern n=10, p=0.3. Man simuliere 1000 zufällige
# Werte für X. Man schätze a) die Wahrscheinlichkeit, dass P(3< X< 7) ; b) den Erwartungswert von X; c) die
# Varianz von X. Man vergleiche die erhaltenen Ergebnisse mit den theoretischen Werten.

import numpy as np
from scipy.stats import binom

n = 10
p = 0.3
sims = 1000

x = np.random.binomial(n, p, sims)

print("a) P(3 < X < 7) = ", np.sum((x > 3) & (x < 7)) / sims)
print("b) E(X) = ", np.mean(x))
print("c) Var(X) = ", np.var(x))

print("Theoretical P(3 < X < 7) =", binom.cdf(6, n, p) - binom.cdf(2, n, p))
print("Theoretical E(X) =", n * p)
print("Theoretical Var(X) =", n * p * (1 - p))
