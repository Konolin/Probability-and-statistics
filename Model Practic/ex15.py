# Man würfelt mit einem Würfel so lange bis das erste Mal die 6 auftaucht. Anhand von Simulationen
# schätze man: wie oft muss man im Mittel (durchschnittlich) würfeln bevor erstmals die 6 auftaucht?
import random

num_sims = 10000
total_rolls = 0
for _ in range(num_sims):
    tries = 1
    current = random.randint(1, 6)
    while current != 6:
        tries += 1
        current = random.randint(1, 6)
    total_rolls += tries
print("Durchschnittliche Anzahl an Würfen:", total_rolls / num_sims)
