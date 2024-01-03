# Die Lebensdauer eines elektronischen Gerätes werde als normalverteilt angenommen. Der Erwartungswert
# betrage 10000 Stunden, und die Standardabweichung 200 Stunden.
# Zufallsgröße X = die Lebensdauer des elektronischen Gerätes.
from scipy.stats import norm

mu = 10000  # Erwartungswert
sigma = 200  # Standardabweichung
n = 10  # Anzahl der simulierten Werte

# a) Simuliere N=10 mögliche Werte von X.
x = norm.rvs(mu, sigma, n)
print(x)

# b) Wie groß ist die theoretische Wahrscheinlichkeit, dass ein zufällig der Produktion entnommenes
print(f"Probability of more than 1500 hours: {sum(x > 1500) / n}")
print(f"Probability of max than 6500 hours: {sum(x <= 6500) / n}")
print(f"Probability of between 7500 and 10500 hours: {sum((x > 7500) & (x <= 10500)) / n}")
