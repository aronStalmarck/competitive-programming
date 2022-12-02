#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

double sum(ll *A, int sz) {
    double ans = 0.0;
    for (int i = 0; i < sz; i++) {
        ans += A[i];
    }
    return ans;
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);
	cin.exceptions(cin.failbit);

    int N, M, K;
    cin >> N >> M >> K;
    int sz = N * M + 1;
    ll count[sz] = {0};
    count[0] = 1;

    for (int dice = 0; dice < N; dice++) {
        ll new_count[sz] = {0};
        for (int val = 1; val < M + 1; val++) {
            for (int i = 0; i < sz; i++) {
                if (i + val > N * M)
                    break;
                new_count[i + val] += count[i];
            }
        }
        memcpy(count, new_count, sizeof(count));
    }
    sort(count, count + sz);
    double ans = 0.0;
    for (int i = 1; i < K + 1; i++)
        ans += count[sz - i] / sum(count, sz);
    cout << setprecision(8) << ans << endl;
}