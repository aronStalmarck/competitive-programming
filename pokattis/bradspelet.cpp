#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); i++)
#define revrep(i, a, b) for(int i = a; i > (b); i--)
#define trav(it, x) for (auto& it : x)
#define print(A) for (auto& x : A) cout << x << ' '; cout << '\n'
#define deb(x) cout<<#x<<'='<<x<<endl
#define deb2(x, y) cout<<#x<<'='<<x<<' '<<#y<<'='<<y<<endl
#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pii;
typedef map<int, int> mii;

const int INF = (int) 1e9;

int N, M;
bool winning_position[101 * 101] = {false};

int idx(int i, int j) {
    return i * M + j;
}

bool is_winning_position(int n, int m) {
    rep(i, 1, n)
        if (!winning_position[idx(i, m)] && !winning_position[idx(n - i, m)])
            return true;
    rep(j, 1, m)
        if (!winning_position[idx(n, j)] && !winning_position[idx(n, m - j)])
            return true;
    return false;
}

int main()
{
    cin.sync_with_stdio(0); cin.tie(0);
	cin.exceptions(cin.failbit);
    cin >> N >> M;
    rep(i, 1, N+1)
        rep(j, 1, M+1)
            winning_position[idx(i, j)] = is_winning_position(i, j);
    if (winning_position[idx(N, M)])
        cout << "A" << endl;
    else
        cout << "B" << endl;
}