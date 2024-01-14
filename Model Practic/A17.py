import numpy as np
import random
# simulations = 500
# X = ['A', 'B']
# P = [0.46, 0.54]
#
# votes = np.random.choice(X, size=simulations, p=P)
#
# votes_for_A = np.sum(votes == 'A')
# prob = votes_for_A / simulations
# print(prob)


total_umfragen = 500
candidateA_chance = 0.46
simulations = 1000
votes_required = 235
count = 0


def simulation_surveys():
    return sum(random.random() < candidateA_chance for _ in range(total_umfragen))

for _ in range(simulations):
    votesA = simulation_surveys()
    if votesA > votes_required:
        count += 1

probability = count / simulations

print(probability)
