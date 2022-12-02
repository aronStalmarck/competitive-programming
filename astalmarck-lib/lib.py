# TEMPLATE - Not one that is commonly used in competitive programming

def main():
    pass

if __name__ == "__main__":
    main()

# ALGORITHMS

# Longest Increasing Subsequence, 2 different approaches

# O(nlogn)
from bisect import bisect_left
def LIS_greedy(n, arr):
    end = [float("inf")]
    for i in range(n):
        idx = bisect_left(end, arr[i])
        if idx == 0:
            end[0] = arr[i]
        elif idx == len(end):
            end.append(arr[i])
        else:
            end[idx] = arr[i]
    return len(end)

# O(n**2)
def LIS_iterative_dp(n, arr):
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)

# Longest Decreasing Subsequence
# O(nlogn)
def LDS(n, arr):
    LIS_greedy(n, [-x for x in arr])


# DFS 
def DFS(start, graph):
    # graph is an adj list
    sz = len(graph)
    visited = [False] * sz
    visited[start] = True
    stack = [start]
    while stack:
        cur = stack.pop()

        # Do something

        for adj in graph[cur]:
            if not visited[adj]:
                stack.append(adj)
                visited[adj] = True


# BFS
from collections import deque
def BFS(start, graph):
    # graph is adj list
    sz = len(graph)
    visited = [False] * sz
    q = deque([start])
    while q:
        cur = q.popleft()
        visited[cur] = True

        # Do something

        for adj in graph[cur]:
            if not visited[adj]:
                q.append(adj)


# Dijkstra O(V + ElogE)
import heapq
def dijkstra(start, graph):
    # graph of adjacency list with tuples: graph[current_node] = [(adj_node, weight), ... ]
    sz = len(graph)
    visited = [False] * sz
    dis = [float("inf")] * sz
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
    # dis is a list of distances from start to all nodes in the graph, prev[v] gives the node previous to v on the shortest path from start to v
    return dis, prev
    


# DATA STRUCTURES


# SegmentTree
class SegmentTree:
    # common bug is wrong standardval
    # consider adding standardans in query()
    def __init__(self, sz, A, standardval, func):
        self.A = [standardval] * (sz * 2)
        self.sz = sz
        self.func = func
        self.standardval = standardval
        for i in range(sz):
            self.A[i + sz] = A[i]
        for i in range(sz - 1, 0, -1):
            self.A[i] = func(self.A[i << 1], self.A[i << 1 | 1])

    def updateNode(self, ind, val):
        ind += self.sz
        self.A[ind] = val
        while ind > 1:
            self.A[ind >> 1] = self.func(self.A[ind], self.A[ind ^ 1])
            ind >>= 1

    def query(self, l, r):
        ans = self.standardval
        l += self.sz
        r += self.sz
        while l < r:
            if l & 1:
                ans = self.func(ans, self.A[l])
                l += 1
            if r & 1:
                r -= 1
                ans = self.func(ans, self.A[r])
            l >>= 1
            r >>= 1
        return ans

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.A[key + self.sz]
        else:
            # is slice
            return self.query(key.start, key.stop)
    def __setitem__(self, key, val):
        self.updateNode(key, val)
    def __repr__(self):
        return f"{self.A[self.sz:]}"

def run_test():
    A = list(range(10))
    # make a segtree of length 10, from the list A, with standardvalue of 0 (usually 0, inf or -inf), and a lambda function returning the sum of a and b
    segtree = SegmentTree(10, A, 0, lambda a, b: a + b)
    # prints the elements in the array that the segtree works on
    print(segtree)
    # print the sum of all elements from (including) index 0 to (but not including) index 5, i.e., [0, 5)
    print(segtree.query(0, 5)) 
    # update node at index 0 to 10
    print(segtree.updateNode(0, 10))

    # segtree[4] = 15 works as expected
    # print(segtree[3]) works as expected
    # print(segtree[2:6]) works as expected

# Union Find
class UnionFind:
    # Add bijection/map to map node in graph to union find index
    def __init__(self, sz):
        self.repr = [i for i in range(sz)]
        self.rank = [1] * sz
        self.sz = sz
        self.numComponents = sz
    
    def find(self, a):
        # find root
        root = a
        while root != repr[root]:
            root = repr[root]
        # compress path
        while a != root:
            next = repr[a]
            repr[a] = root
            a = next
        return root
    
    def connected(self, a, b):
        return self.find(a) == self.find(b)
    
    def componentSz(self, a):
        return self.rank[self.find(a)]

    def unify(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        # make b into the larger number
        if self.rank[a] > self.rank[b]:
            self.swap(a, b)
        # merge smaller component into larger component
        self.rank[b] += self.rank[a]
        self.repr[a] = b
        self.numComponents -= 1

# Random set with fast insertion and deletion
from random import randint
class RandomSet:
    def __init__(self):
        self.dict = {}
        self.list = []

    def add(self, item):
        if item not in self.dict:
            self.dict[item] = len(self.list)
            self.list.append(item)

    def addIterable(self, item):
        for a in item:
            self.add(a)

    def delete(self, item):
        if item in self.dict:
            index = self.dict[item]
            if index == len(self.list)-1:
                del self.dict[self.list[index]]
                del self.list[index]
            else:
                self.list[index] = self.list.pop()
                self.dict[self.list[index]] = index
                del self.dict[item]

    def getRandom(self):
        if self.list:
            return self.list[randint(0,len(self.list)-1)]

    def popRandom(self):
        if self.list:
            index = randint(0,len(self.list)-1)
            if index == len(self.list)-1:
                del self.dict[self.list[index]]
                return self.list.pop()
            returnValue = self.list[index]
            self.list[index] = self.list.pop()
            self.dict[self.list[index]] = index
            del self.dict[returnValue]
            return returnValue