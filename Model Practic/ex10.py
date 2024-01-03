import numpy as np
from scipy.stats import norm

# Die Zufallsvariable X sei normalverteilt mit Erwartungswert gleich 3 und Varianz gleich 4.
# Man schätze P(|X| > 4) anhand von

x = 3  # Erwartungswert
v = 4  # Varianz
n = 1000  # Anzahl der Simulationen

# (a) Simulationen
x = np.random.normal(x, np.sqrt(v), n)
print("P(|x| > 4) = ", np.mean(np.abs(x) > 4))

# (b) spezifischen Anweisungen der Normalverteilung.
print("P(|x| > 4) = ", 2 * (1 - norm.cdf(4, x, np.sqrt(v))))
