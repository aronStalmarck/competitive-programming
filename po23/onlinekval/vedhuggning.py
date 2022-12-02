class Tree:
    def __init__(self, params):
        self.starting_length, self.growth_speed, self.max_time = params

    def get_length(self, t):
        return self.starting_length + self.growth_speed * min(t, self.max_time)

def binary_search(f, L, R):
    ans = -1
    while L <= R:
        m = int((L + R) / 2)
        if f(m):
            ans = m
            R = m - 1
        else:
            L = m + 1
    return ans

N, S = [int(i) for i in input().split()]
trees = [Tree([int(i) for i in input().split()]) for _ in range(N)]

def check(t):
    return sum((tree.get_length(t) for tree in trees)) >= S
        
print(binary_search(check, 0, 10**9))