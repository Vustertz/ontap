from python_library import array_input
import itertools
import statistics
import heapq
import math

# n = array_input()

# for i in itertools.permutations(n):
#     print(i)

# print(statistics.mode(n))

# print(heapq.heapify(n))

# print(math.gcd(n[0], n[1]))
# print(math.lcm(n[0],n[1]))

# n = int(input())
# gia_tien = 0
# if n > 10:
#     gia_tien += (n - 10) * 7000 + 10 * 4000
# print(gia_tien)
t  = str(input())
have = {}
for i in t:
    if i not in have:
        have[i] = 1
    else:
        have[i] += 1
print(have)