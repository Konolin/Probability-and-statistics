import random
import numpy
from matplotlib.pyplot import bar, show, hist, grid, legend, xticks


def ex1_1():
    num_simulations = 1000
    red_count = 6
    blue_count = 4
    green_count = 6
    successful_a = 0
    successful_b = 0
    successful_ab = 0
    for _ in range(num_simulations):
        balls = random.sample(['r', 'b', 'g'], counts=[red_count, blue_count, green_count], k=3)
        extracted_balls = random.sample(balls, k=3)
        if 'r' in extracted_balls:
            successful_a += 1

        if extracted_balls[0] == extracted_balls[1] == extracted_balls[2]:
            if 'r' in extracted_balls:
                successful_ab += 1
            successful_b += 1

    print(f"A: P(A) = {successful_a / num_simulations}")
    print(f"B: P(B) = {successful_b / num_simulations}")
    print(f"C: P(A and B) = {successful_ab / num_simulations}")
    print(f"D: P(B|A)= {(successful_ab / num_simulations) / (successful_a / num_simulations)}")


def ex1_2():
    #           not red extracted
    th_A = 1 - (10 / 16 * 9 / 15 * 8 / 14)
    #      all red                    all blue                  all green
    th_B = (6 / 16 * 5 / 15 * 4 / 14) + (4 / 16 * 3 / 15 * 2 / 14) + (6 / 16 * 5 / 15 * 4 / 14)
    th_AB = 6 / 16 * 5 / 15 * 4 / 14
    th_BA = th_AB / th_A

    print(f"Theoretical probability P(A) = {th_A}")
    print(f"Theoretical probability P(B) = {th_B}")
    print(f"Theoretical probability P(A and B) = {th_AB}")
    print(f"Theoretical probability P(B|A) = {th_BA}")


def ex2():
    n = 20000
    data = [random.randrange(1, 7) for _ in range(n)]
    results, count = numpy.unique(data, return_counts=True)
    d = dict([(results[i], count[i] / n) for i in range(0, 6)])
    print(d)
    bar(results, count / n, width=0.9, color="red", edgecolor="black", label="Relative probability")
    d = dict([(k, 1 / 6) for k in range(1, 7)])
    bar(d.keys(), d.values(), width=0.7, color="blue", edgecolor="black", label="Theoretical probability")
    legend(loc="lower left")
    xticks(range(0, 7))
    grid()
    show()


def ex3():
    simulations_count = 500
    dice1 = [random.randrange(1, 7) for _ in range(simulations_count)]
    dice2 = [random.randrange(1, 7) for _ in range(simulations_count)]
    dice3 = [random.randrange(1, 7) for _ in range(simulations_count)]
    dice_sums = []
    for i in range(simulations_count):
        dice_sums.append(dice1[i] + dice2[i] + dice3[i])

    results, count = numpy.unique(dice_sums, return_counts=True)
    relative_probability = dict([(results[i], count[i] / simulations_count) for i in range(len(results))])
    bar(results, count / simulations_count, width=0.9, color="red", edgecolor="black", label="Relative probability")

    best_choices_array = best_choices(count)
    print(f"Best relative choice: {best_choices_array}")

    dice_sums = []
    for i in [1, 2, 3, 4, 5, 6]:
        for j in [1, 2, 3, 4, 5, 6]:
            for k in [1, 2, 3, 4, 5, 6]:
                dice_sums.append(i + j + k)

    results, count = numpy.unique(dice_sums, return_counts=True)
    bar(results, count / (6 * 6 * 6), width=0.7, color="blue", edgecolor="black", label="Theoretical probability")

    best_choices_array = best_choices(count)
    print(f"Best theoretical choice: {best_choices_array}")

    legend(loc="lower left")
    xticks(range(0, 19))
    grid()
    show()


def best_choices(count):
    max_count = max(count)
    max_positions = []
    for i in range(len(count)):
        if count[i] == max_count:
            max_positions.append(i + 3)
    return max_positions


def main():
    # ex1_1()
    # ex1_2()
    # ex2()
    ex3()


if __name__ == "__main__":
    main()
