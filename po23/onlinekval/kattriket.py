from heapq import heappop, heappush
from sys import setrecursionlimit
setrecursionlimit(10000000)

# Input
N = int(input())

graph = [[] for _ in range(N)]
for i in range(N-1):
    u, v = [int(i) for i in input().split()]
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(N)]

#
child_nodes = [[] for _ in range(N)]

def dfs_ch_p(cur):
    if visited[cur]:
        return 0
    visited[cur] = True
    p = 0
    for ch in graph[cur]:
        if not visited[ch]:
            ch_p = dfs_ch_p(ch) + 1
            child_nodes[cur].append((ch_p, ch))
            p = max(p, ch_p)
    return p

dfs_ch_p(0)
child_nodes = [sorted(ch_of_u) for ch_of_u in child_nodes]

# pq = [(-ch_p, u), ...]
cur = 0
new_branches = []
count = 1
output = []
for i in range(1, N):
    # Add ch of cur to possible new branches except the one with longest path
    for ch_p, ch in child_nodes[cur][:-1]:
        heappush(new_branches, (-ch_p, ch))
    # Go to child node with longest path if it is possible
    if child_nodes[cur]:
        cur = child_nodes[cur].pop()[1]
    # Go to a new branch
    else:
        cur = heappop(new_branches)[1]
        count += 1
    output.append(count)
    #print(cur, new_branches)
print(*output)
    




