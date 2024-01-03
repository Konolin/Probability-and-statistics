# Man schätze anhand von Simulationen die Wahrscheinlichkeit, dass man in einem Lottospiel (mit Zahlen
# von 1 bis 49, 6 Zahlen werden ohne Zurücklegen gezogen) genau 2 Zahlen richtig erratet.
import random

num_sims = 10000
count = 0
correct_numbers = random.sample(range(1, 50), k=6)
for _ in range(num_sims):
    numbers = random.sample(range(1, 50), k=2)
    if numbers[0] in correct_numbers and numbers[1] in correct_numbers:
        count += 1
print(f"Probability: {count / num_sims}")
