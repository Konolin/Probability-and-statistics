import numpy as np

num_simulations = 1000
num_games = 10
total_wins = 0

for _ in range(num_simulations):
    current_wins = 0
    for _ in range(num_games):
        x = np.random.randint(1, 38)
        if x == 15:
            current_wins += 175
        else:
            current_wins -= 5
    total_wins += current_wins

print(f"Average wins in {num_simulations} simulations: {total_wins / num_simulations}")
