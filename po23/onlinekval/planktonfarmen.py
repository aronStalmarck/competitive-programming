A, N, lengths = int(input()), int(input()), sorted([int(i) for i in input().split()])
for i in range(N):
    if i < len(lengths) - 1 and lengths[i] * lengths[-1] >= A:
        lengths.pop()
print(N - len(lengths))