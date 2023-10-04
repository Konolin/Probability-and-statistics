import random
from random import sample
import math
from math import factorial, perm, comb
import itertools
from itertools import permutations, combinations

print(perm(4, 4))  # 24
print(perm(4, 2))  # 12

# help(itertools.permutations)
s = "ABC"
permS = list(permutations(s))
print(permS)

print(factorial(len(permS)))

s = "MATHE"
print(sample(s, 5))
print(sample(s, 3))

print(list(combinations(s, 3)))

print(len(list(combinations("ABC", 3))))


