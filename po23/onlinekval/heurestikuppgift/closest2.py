class Point:
    def __init__(self, params, id):
        self.x, self.y = params[0], params[1]
        self.id = id

    def __repr__(self) -> str:
        return f"p{self.id}: ({self.x}, {self.y})"

def distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def min_dist(cur, points, sample_size):
    sample = [points.pop() for _ in range(min(sample_size, len(points)))]
    d, to = min([(distance(p, cur), p) for p in sample])
    for p in sample:
        if p.id == to.id:
            continue
        points.add(p)
    return d, to

T, N = int(input()), int(input())
points = set([Point([int(i) for i in input().split()], idx + 1) for idx in range(N)])

cur = points.pop()
path = [cur]
for choice in range(int(N / 2 - 1)):
    d, cur = min_dist(cur, points, 100)
    path.append(cur)

print(" ".join(str(x.id) for x in path))