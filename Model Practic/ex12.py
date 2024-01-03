# Ein sechsseitiger Würfel wird auf vier Seiten mit einer 1 und auf zwei Seiten mit einer 2 übermalt. Er wird
# zweimal geworfen.
# 1) Die Zufallsvariable X gibt die Summe der erhaltenen Zahlen an. Man gebe alle möglichen Werte von X an und
# die entsprechenden theoretischen Wahrscheinlichkeiten.
# 2) Anhand von Simulationen schätze man
# 2a) die zu erwartende Summe (d.h. E(X)) ; 2b) die Wahrscheinlichkeit dafür, dass die Summe größer als 2 ist.
import random

num_sims = 1000
sum_2 = 0
sum_3 = 0
sum_4 = 0
for _ in range(num_sims):
    data = random.choices([1, 2], weights=[4/6, 2/6], k=2)
    if sum(data) == 2:
        sum_2 += 1
    elif sum(data) == 3:
        sum_3 += 1
    elif sum(data) == 4:
        sum_4 += 1

print(f"Summe 2: {sum_2/num_sims}")
print(f"Summe 3: {sum_3/num_sims}")
print(f"Summe 4: {sum_4/num_sims}")
print(f"Theoretische Wahrscheinlichkeit Summe 2:", 4/6 * 4/6)
print(f"Theoretische Wahrscheinlichkeit Summe 3:", 4/6 * 2/6 + 2/6 * 4/6)
print(f"Theoretische Wahrscheinlichkeit Summe 4:", 2/6 * 2/6)

