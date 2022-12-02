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

int main()
{
    cin.sync_with_stdio(0); cin.tie(0);
    cin.exceptions(cin.failbit);

    int T, N;
    
    cin >> T >> N;
    if (T > 1)
        return 0;
    vvi points;
    rep(i, 0, N) {
        int x, y;
        cin >> x >> y;
        points.push_back({x, y, i + 1});
    }
    sort(points.begin(), points.end());

    int min_path_len = INF;
    vi best_path;
    rep(start, 0, N/2 + 1) {
        int p_len = 0;
        vi path = {points[start][2]};
        int cur = start;
        rep(to, cur + 1, cur + N/2) {
            p_len += abs(points[cur][0] - points[to][0]);
            path.pb(points[to][2]);
        }
        if (p_len < min_path_len) {
            best_path = path;
        }        
    }
    trav(x, best_path) {
        cout << x << " ";
    }
    cout << endl;
    
}