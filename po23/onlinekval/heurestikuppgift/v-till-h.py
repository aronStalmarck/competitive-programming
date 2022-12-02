# Group 1: 9.95
# Group 2: 7.1
class Point:
    def __init__(self, params, id):
        self.x, self.y = params[0], params[1]
        self.id = id

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

T, N = int(input()), int(input())
points = [Point([int(i) for i in input().split()], idx + 1) for idx in range(N)]

y_max, y_min = max([p.y for p in points]), min([p.y for p in points])
y_mid = (y_max + y_min) / 2
y_delta = y_max - y_mid
y_mean = sum((p.y for p in points)) / N
y_median = sorted([p.y for p in points])[int(N/2)]

points_mid = [p for p in points if abs(p.y - (y_mean)) < (y_max - y_min) / 3.7]


if len(points_mid) >= N/2:
    points_mid.sort(key=lambda p: (p.x, p.y))
    print(*[p.id for p in points_mid[:int(N/2)]])

else:
    points.sort(key=lambda p: (p.x, p.y))
    print(*[p.id for p in points[:int(N/2)]])
