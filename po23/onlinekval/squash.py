N, K = [int(i) for i in input().split()]
arr = [1 if m == "V" else -1 for m in input()]

dp = [[0 for _ in range(N+1)] for _ in range(K+2)]

def f(start, k):
    ans, val = 0, 0
    for i in range(start, N):
        val += arr[i]
        ans = max(val + dp[k+1][i+1], ans)
    return ans

for k in range(K, 0, -1):
    for i in range(N-1, -1, -1):
        dp[k][i] = max(dp[k + 1][i], dp[k][i + 1], f(i, k))
            
print(dp[1][0])


