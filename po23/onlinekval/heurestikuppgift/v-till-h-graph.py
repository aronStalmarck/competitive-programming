import numpy as np

class Point:
    def __init__(self, params, id):
        self.x, self.y = params[0], params[1]
        self.id = id

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

def distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def build_graph(points, num_edges):
    sz = len(points)
    graph = [[] for _ in range(sz)]
    for u in range(sz):
        for v in range(u + 1, min(u + num_edges + 1, sz)):
            graph[u].append((v, distance(points[u], points[v])))
    return graph


def find_path(graph):
    sz = len(graph)
    # dist[i][k] = when chosen k

    dist = [[0] + [float("inf")] * (int(sz/2) - 1)  for _ in range(sz)]
    prev = [[-1] * (int(sz/2)) for _ in range(sz)]
    for u in range(sz-1, -1, -1):
        for v, w in graph[u]:
            for k in range(1, int(sz/2)):
                if dist[v][k - 1] + w < dist[u][k]:
                    dist[u][k] = dist[v][k-1] + w
                    prev[u][k] = v
    cur = np.argmin([d[-1] for d in dist])
    path = [cur]

    for i in range(int(sz/2)-1, 0, -1):
        cur = prev[cur][i]
        path.append(cur)
    return path, min([d[-1] for d in dist])





T, N = int(input()), int(input())
points = [Point([int(i) for i in input().split()], idx + 1) for idx in range(N)]

points.sort(key=lambda p: (p.x, p.y))

graph = build_graph(points, 40)
p, p_len = find_path(graph)

print(*[points[u].id for u in p])