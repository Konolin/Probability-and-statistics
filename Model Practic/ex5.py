import matplotlib.pyplot as plt
import numpy as np

# Stichprobenvariablen in Histogrammen dargestellt: für die im Vektor X gegebenen Daten zeichne man das
# Histogramm der absoluten, bzw. relativen Häufigkeiten. Man gebe an P(X<301).

x = [299, 299, 297, 303, 299, 301, 300, 297, 302, 303, 300, 299, 301, 302, 301, 299, 300, 297, 300, 300, 296, 303, 295,
     295, 297]

# a) Histogramm der absoluten Häufigkeiten
plt.hist(x, bins=range(min(x), max(x) + 1))
plt.show()

# b) Histogramm der relativen Häufigkeiten
plt.hist(x, bins=range(min(x), max(x) + 1), density=True)
plt.show()

# c) P(X<301)
print(f"P(X<301) = {np.sum(np.array(x) < 301) / len(x)}")
