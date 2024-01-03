# In einer Urne befinden sich 6 rote, 4 weiße und 10 blaue Kugeln. Es werden vier Kugeln gezogen. Wie groß
# ist die Wahrscheinlichkeit, die Kugeln in der Reihenfolge „rot, weiß, blau, blau" zu ziehen, wenn die Kugeln nach
# der Ziehung
# a) zurückgelegt b) nicht zurückgelegt werden?
# Man beantworte die Fragen anhand von Simulationen; welche sind die entsprechenden theoretischen
# Wahrscheinlichkeiten?
import random

import numpy as np

num_sims = 1000
correct_count = 0
for _ in range(num_sims):
    data = random.sample(["red", "white", "blue"], counts=[6, 4, 10], k=4)
    correct_count += 1 if data == ["red", "white", "blue", "blue"] else 0
print(f"Probability without replacement: {correct_count / num_sims}")

correct_count = 0
for _ in range(num_sims):
    data = random.choices(["red", "white", "blue"], weights=[6, 4, 10], k=4)
    correct_count += 1 if data == ["red", "white", "blue", "blue"] else 0
print(f"Probability with replacement: {correct_count / num_sims}")

print(f"Theoretical probability without replacement: {6 / 20 * 4 / 19 * 10 / 18 * 9 / 17:.2f}")
print(f"Theoretical probability with replacement: {6 / 20 * 4 / 20 * 10 / 20 * 10 / 20:.2f}")
