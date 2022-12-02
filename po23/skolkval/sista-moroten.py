from math import ceil
import heapq

N, M, K = [int(i) for i in input().split()]

count = [0 for _ in range(N * M + 1)]
count[0] = 1

for dice in range(N):
    new_count =  [0 for _ in range(N * M + 1)]
    for val in range(1, M + 1):
        for i in range(0, N * M + 1):
            if i + val < len(count):
                new_count[i + val] += count[i]
    count = new_count
new_count =  [0 for _ in range(N * M + 1)]

count.sort()

print(sum(count[-K:]) / sum(count))