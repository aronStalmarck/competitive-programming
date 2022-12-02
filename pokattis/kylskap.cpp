#include<stdio.h>

int memo[1001];
bool A[1001] = {false};

int pa, ka, pb, kb, n;

int min(int x, int y) {
    if (x < y)
        return x;
    return y;
}

int dp(int i) {
    if (i <= 0)
        return 0;
    if (memo[i] != -1)
        return memo[i];
    memo[i] = min(dp(i - ka) + pa, dp(i - kb) + pb);
    if (memo[i] == dp(i - ka) + pa)
        A[i] = true;
    return memo[i];
}

int main() {
    scanf("%d %d %d %d %d", &pa, &ka, &pb, &kb, &n);
    for (int i = 0; i < 1001; i++) {
        memo[i] = -1;
    }
    int ans = dp(n);
    int a = 0, b = 0, i = n;
    while (i > 0) {
        if (A[i]) {
            a++;
            i -= ka;
        } else {
            b++;
            i -= kb;
        }
    }
    printf("%d %d %d", a, b, ans);
}