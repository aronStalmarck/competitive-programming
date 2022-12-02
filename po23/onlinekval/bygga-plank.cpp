#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); i++)
#define revrep(i, a, b) for(int i = a; i > (b); i--)
#define trav(it, x) for (auto& it : x)
#define print(A) for (auto& x : A) cout << x << ' '; cout << '\n'
#define deb(x) cout<<#x<<'='<<x<<endl
#define deb2(x, y) cout<<#x<<'='<<x<<' '<<#y<<'='<<y<<endl
#define aint(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define sz(a) ((int) a.size())

typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pii;
typedef map<int, int> mii;

const int INF = (int) 1e9;
const int max_sz = 100000;

// Segment Tree
struct SegmentTree{
    int *arr;
    int size;
    const int standardVal = 0;
    SegmentTree(int n){
        size = n;
        arr = new int[2 * n];
        rep(i, 0, n * 2) {
            arr[i] = 0;
        }
    }
    void updateNode(int idx, int val){
        idx += size;
        arr[idx] = val;
        while (idx > 1){
            arr[idx >> 1] = arr[idx] + arr[idx ^ 1];
            idx >>= 1;
        }
    }
    int query(int l, int r){
        int ans = standardVal;
        l += size;
        r += size;
        while (l < r){
            if (l & 1){
                ans += arr[l];
                l++;
            }
            if (r & 1){
                r--;
                ans += arr[r];
            }
            l >>= 1;
            r >>= 1;
        }
        return ans;
    }
};

int main()
{
    cin.sync_with_stdio(0); cin.tie(0);
    cin.exceptions(cin.failbit);
    int N, K;
    cin >> N >> K;
    vector<int> H;
    rep(i, 0, N) {
        int h; cin >> h; H.pb(h);
    }
    SegmentTree st = SegmentTree(N);
    vector<pii> H_ordered(N);

    rep(i, 0, N)
        H_ordered[i] = mp(H[i], i);
    sort(H_ordered.begin(), H_ordered.end());
    reverse(H_ordered.begin(), H_ordered.end());

    long long max_area = 0, j = 0;
    rep(i, 0, N) {
        int h = H_ordered[i].first, x = H_ordered[i].second;
        while (j < N && H_ordered[j].first >= h) {
            st.updateNode(H_ordered[j].second, 1);
            j++;
        }
        int w_left[21] = {0}, w_right[21] = {0};
        
        rep(k, 0, K+1) {
            int R = x - 1;
            int L = 0, w = 0;
            while (L <= R) {
                int m = (int) (L + R) / 2;
                if (st.query(m, x) < (x - m - k)) {
                    L = m + 1;
                }  
                else {
                    w = x - m;
                    R = m - 1;
                }
                    
            }
            w_left[k] = w;
        }
        
        rep(k, 0, K+1) {
            int L = x + 1;
            int R = N - 1, w = 0;
            while (L <= R) {
                int m = (L + R) / 2;
                if (st.query(x + 1, m+1) < m - x - k) {
                    R = m - 1;
                }  
                else {
                    w = m - x;
                    L = m + 1;
                }
                    
            }
            w_right[k] = w;
        }
        vector<long long> areas;
        rep(i, 0, K+1) {
            areas.pb((long long) h * (w_left[i] + 1 + w_right[K-i])) ;
        }
        max_area = max(*max_element(areas.begin(), areas.end()), max_area);
    }
    cout << max_area << endl;
}
