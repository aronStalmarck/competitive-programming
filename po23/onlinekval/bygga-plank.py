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

    def increment(self, ind):
        ind += self.sz
        self.A[ind] += 1
        while ind > 1:
            self.A[ind >> 1] = self.func(self.A[ind], self.A[ind ^ 1])
            ind >>= 1

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

N, K = [int(i) for i in input().split()]
H = [int(i) for i in input().split()]

# st[i] = 1 if H[i] >= h else 0
st = SegmentTree(N, [0] * N, 0, lambda a, b: a + b)

H_ordered = sorted([(height, idx) for idx, height in enumerate(H)], reverse=True)

max_area = 0
j = 0

for i in range(N):
    # choose H_ordered[i]
    h, x = H_ordered[i]
    # Add all H[j] where H[j] >= h

    while j < N and H_ordered[j][0] >= h:
        st.updateNode(H_ordered[j][1], 1)
        j += 1
    w_left, w_right = [], []
    # check left
    for k in range(K+1):
        L = 0
        R = x - 1
        w = 0
        while L <= R:
            m = int((L + R) / 2)
            if st.query(m, x) + k >= (x - m):
                w = x - m
                R = m - 1
            else:
                L = m + 1
        w_left.append(w)
    # check right
    for k in range(K+1):
        L = x + 1
        R = N - 1
        w = 0
        while L <= R:
            m = int((L + R) / 2)
            if st.query(x + 1, m+1) + k >= m - x:
                w = m - x
                L = m + 1
            else:
                R = m - 1
        w_right.append(w)
    # get max
    max_area = max(max((w_left[i] + 1 + w_right[K - i] for i in range(0, K+1))) * h, max_area)

print(max_area)
        

