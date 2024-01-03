# Eine Maschine produziert im Mittel 10mm lange Schrauben mit einer Standardabweichung von 1mm. Die
# Länge der Schrauben kann als normalverteilt angesehen werden. Anhand von (a) Simulationen (b) spezifischen
# Anweisungen berechne man die geschätzte bzw. theoretische Wahrscheinlichkeit dafür, dass
# • eine Schraube kürzer ist als 9 mm;
# • eine Schraube höchstens 10.1 mm und mindestens 8.9 mm lang ist;
import numpy as np
from scipy.stats import norm

mu = 10
sigma = 1
simulations = 1000
data = norm.rvs(mu, sigma, simulations)

print(f"Probability shorter than 9mm (Simulations): {np.mean(np.array(data < 9)):.2f}")
print(f"Probability between 10.1mm and 8.9 (Simulations): "
      f"{np.mean(np.array(data < 10.1) & np.array(data > 8.9)):.2f}")
print(f"Probability shorter than 9mm (Theoretical): {norm.cdf(9, loc=mu, scale=sigma):.2f}")
print(f"Probability between 10.1mm and 8.9 (Theoretical): "
      f"{norm.cdf(10.1, loc=mu, scale=sigma) - norm.cdf(8.9, loc=mu, scale=sigma):.2f}")
