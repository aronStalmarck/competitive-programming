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

#define inf 1e9
typedef pair<int, int> Edge; // node, weight 
typedef vector<vector<Edge>> Graph; //

void find_path(Graph G, int* x, int* y) {
    
}

int main()
{
    cin.sync_with_stdio(0); cin.tie(0);
    cin.exceptions(cin.failbit);

    int T, N;
    cin >> T >> N;

    int x[N], y[N];
    rep(i, 0, N) {
        cin >> x[i] >> y[i];
    }

    vvi points(N);
    rep(i, 0, N) {
        points[i] = {x[i], y[i], i};
    }
    sort(points.begin(), points.end());
    
    Graph G;
    rep(i, 0, N) {
        rep(j, i + 1, min(i + 20, N)) {
            G[i].pb({j, abs(x[i] - x[j]) + abs(y[i] - y[j])});
        }
        revrep(j, i - 1, max(i - 20, 0)) {
            G[i].pb({j, abs(x[i] - x[j]) + abs(y[i] - y[j])});
        }
    }

    
}