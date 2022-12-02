N = int(input())

# INPUT
H = [0]

tr = dict()

for i in range(1, N + 1):
    H.append(int(input()))
    for t in input():
        tr[t] = tr.get(t, []) + [i]

# Make graph - adj list
G = [[] for _ in range(N +1)]

for i in range(1, N+1):
    for (t, nodes) in tr.items():
        if i in nodes:
            for adj in nodes:
                if adj != i:
                    G[i].append((adj, abs(H[i] - H[adj])))
                    
# Dijkstra O(V + ElogE)
import heapq
def dijkstra(start, graph):
    # graph is adj list with tuples: graph[u] = [(v, w), ... ]
    sz = len(graph)
    visited = [False] * sz
    dis = [1e9] * sz
    prev = [-1] * sz
    dis[start] = 0
    q = [(0, start)]
    while q:
        u = heapq.heappop(q)[1]
        if visited[u]:
            continue
        else:
            visited[u] = True
        for v, w in graph[u]:
            if dis[u] + w < dis[v]:
                dis[v] = dis[u] + w
                prev[v] = u
                heapq.heappush(q, (dis[v], v))
    return dis
    
print(sum((dijkstra(i, G)[i + 1] for i in range(1, N))))

"""
8
1
AB
4
DE
1
CEF
3
AD
2
E
2
D
2
BC
3
F

"""