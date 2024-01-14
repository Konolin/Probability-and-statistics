import random
import numpy as np

playerA_win_prob=0.6
playB_win_prob = 1 - playerA_win_prob
simulations = 2000
games_to_win = 3

playerA_wins = 0
playerB_wins = 0

for _ in range(simulations):
    games_played = 0
    playerA_score = 0
    playerB_score = 0

    while True:
        outcome = random.random()
        if outcome <= playerA_win_prob:
            playerA_score += 1
        else:
            playerB_score += 1

        games_played += 1

        if playerA_score == games_to_win:
            playerA_wins += 1
            break
        elif playerB_score == games_to_win:
            playerB_wins += 1
            break

prob_A_win = playerA_wins / simulations
prob_B_win = playerB_wins / simulations

print(prob_A_win)
print(prob_B_win)
