# Tom schießt auf eine Zielscheibe, und die Wahrscheinlichkeit, mit der sein Schuss die Zielscheibe trifft,
# beträgt p=0.3 (leider ist Tom kein geübter Schütze). Er möchte die Wahrscheinlichkeit für die Anzahl X der
# Schüsse wissen, bis (inklusiv) er zum ersten Mal die Zielscheibe trifft.
# (1) Man zeichne das Histogramm der absoluten Häufigkeiten für die Zufallsgröße X.
# (2) Man bestimme wie viele Schüsse durchschnittlich geschossen werden bis Tom die Zielscheibe trifft.
# (3) Man schätze P(X<5) und vergleiche diese mit der theoretischen Wahrscheinlichkeit.
import numpy as np
import matplotlib.pyplot as plt

# Wahrscheinlichkeit, die Zielscheibe zu treffen
p = 0.3
simulations = 1000  # Anzahl der Simulationen

shots_to_hit = []

for i in range(simulations):
    shots = 1
    while np.random.rand() > p:
        shots += 1
    shots_to_hit.append(shots)

# print(shots_to_hit)

plt.hist(shots_to_hit, bins=max(shots_to_hit), align='mid', rwidth=0.8)
plt.title("Histogramm der Anzahl der Schüsse bis zum Treffer")
plt.xlabel("Anzahl der Schüsse")
plt.ylabel("Absolute Häufigkeit")
plt.show()

average_shots = np.mean(shots_to_hit)
print(f"Durchschnittliche Anzahl der Schüsse: {average_shots}")

# Schätzung von P(X<5)
probability_less_than_5 = np.sum(np.array(shots_to_hit) < 5) / simulations
print(f"Schätzung von P(X<5): {probability_less_than_5}")

# Theoretische Wahrscheinlichkeit P(X<5)
theoretical_probability_less_than_5 = sum([(1-p)**(x-1) * p for x in range(1, 5)])
print(f"Theoretische Wahrscheinlichkeit P(X<5): {theoretical_probability_less_than_5}")
print("I like chicken nuggets")
