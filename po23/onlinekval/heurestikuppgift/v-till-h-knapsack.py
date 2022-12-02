class Point:
    def __init__(self, params, id):
        self.x, self.y = params[0], params[1]
        self.id = id

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

def distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

T, N = int(input()), int(input())
points = [Point([int(i) for i in input().split()], idx + 1) for idx in range(N)]

points.sort(key=lambda p: (p.x, p.y))

# dp[i, k] = maximum value when ending at (and choosing) i and having chosen k-1 before
# p[i, k] = previous from i, k
dp = [[0] + [float("inf")] * int(N/2) for _ in range(N + 1)]
p = [[0] + [float("inf")] * int(N/2) for _ in range(N + 1)]
for i in range(1, int(N + 1)):
    for k in range(1, int(N/2 + 1)):
        for j in range(max(0, i - 10), i):
            if dp[j][k - 1] + distance(points[j], points[i]) < dp[i, k]:
                dp[i] = dp[j][k - 1] + distance(points[j], points[i])
                p[i][k] = j

path = []
cur = -1
