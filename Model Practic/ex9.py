# In einem Programm werden unabhängig voneinander 500 standardnormalverteilte Zufallsvariablen erzeugt
# und aufsummiert. Man schätze die Wahrscheinlichkeit dafür, dass die Summe der erzeugten Zufallsvariablen
# außerhalb des Intervalls [−20, 10] liegt. Man vergleiche das Ergebnis mit der theoretischen Wahrscheinlichkeit
# (Man benutze Octavebefehle für die Normalverteilung!).
# Hinweis: X1,...,X500 ~N(0,1) unabhängige ZG ⇒ X1+...+X500 ~N(0,500)

import numpy as np
from scipy.stats import norm

# Anzahl der Zufallsvariablen
n = 500
simulations = 1000

# Simuliere 1000 Summen von standardnormalverteilten Zufallsvariablen
simulated_sums = np.sum(np.random.randn(n, simulations), axis=0)

print(f'Probability outside intervall (Simulations): {np.mean((simulated_sums < -20) | (simulated_sums > 10)):.4f}')
