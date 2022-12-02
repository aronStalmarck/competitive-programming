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

}
// DATA STRUCTURES

// Segment Tree
struct SegmentTree{
    vi arr;
    ll size;
    ll standardVal;
    function<ll(ll, ll)> func;
    SegmentTree(vi A, ll standardValue, function<ll(ll, ll)> function){
        size = sz(A);
        standardVal = standardValue;
        func = function;
        arr.resize(size * 2, standardVal);
        for (ll i = 0; i < size; i++){
            arr[size + i] = A[i];
        }
        for (ll i = size-1; i > 0; i--){
            arr[i] = func(arr[i << 1], arr[i << 1 | 1]);
        }
    }
    void updateNode(ll idx, ll val){
        idx += size;
        arr[idx] = val;
        while (idx > 1){
            arr[idx >> 1] = func(arr[idx], arr[idx ^ 1]);
            idx >>= 1;
        }
    }
    ll query(ll l, ll r){
        ll ans = standardVal;
        l += size;
        r += size;
        while (l < r){
            if (l & 1){
                ans = func(ans, arr[l]);
                l += 1;
            }
            if (r & 1){
                r -= 1;
                ans = func(ans, arr[r]);
            }
            l >>= 1;
            r >>= 1;
        }
        return ans;
    }
    void print(){
        trav(x, arr){
            cout << x << " ";
        }
        cout << "\n";
    }
};

// UNION FIND

vi id, sz;
ll num_components;

void init(ll n){
    id.clear();
    sz.clear();
    rep(i, 0, n){
        id.pb(i);
        sz.pb(1);
    }
    num_components = n;
}

ll find(ll a){
    ll root = a;
    while (root != id[root]){
        root = id[root];
    }
    while (a != root){
        ll next = id[a];
        id[a] = root;
        a = next;
    }
    return root;
}

bool connected(ll a, ll b){
    return find(a) == find(b);
}

bool compenentSz(ll a){
    return sz[find(a)];
}

void unify(ll a, ll b){
    a = find(a);
    b = find(b);
    if (a == b){
        return;
    }
    // make sure b is larger than a
    if (sz[a] > sz[b]){
        swap(a, b);
    }
    // merge smaller component into larger component
    sz[b] += sz[a];
    id[a] = b;
    num_components--;
}

// Random set with fast insertion, deletion and can get random value
struct RandomSet {
    mii dict;
    int *arr, arr_sz = 0;
    int max_sz;

    RandomSet(int max_sz) {
        arr = new int[max_sz];
    }

    void add(int el) {
        if (dict.count(el)) {
            dict[el] = arr_sz;
            arr[arr_sz++] = el;
        }
    }

    void remove(int el) {
        if (dict.count(el)) {
            int index = dict[el];
            if (index == arr_sz - 1) {
                dict.erase(arr[index]);
                arr_sz--;
            }
            else {
                arr[index] = arr[--arr_sz];
                dict[arr[index]] = index;
                dict.erase(el);
            }
        }
    }

    // make sure that s is 
    int get_random() {
        return arr[rand() % arr_sz];
    }
};

// ALGORITHMS

// Dijkstra's, tror O(E + VlogV)
#define inf 1e9
typedef pair<int, int> Edge; // node, weight 
typedef vector<vector<Edge>> Graph; //

int dijkstra(int start, int goal, Graph graph){
    vector<bool> visited (graph.size(), false);
    vector<int> P (graph.size(), -1);
    vector<int> D (graph.size(), inf);
    D[0] = 0;
    set<pair<int, int>> Q; // Distance, node
    Q.insert({start, 0});
    while (!Q.empty()){
        int cur = (*Q.begin()).second;
        Q.erase(Q.begin());
        if (visited[cur]){
            continue;
        }
        for (Edge adj : graph[cur]){
            int node = adj.first;
            if (visited[node]){
                continue;
            }
            int weight = adj.second;
            if (D[cur] + weight < D[node]){
                D[node] = D[cur] + weight;
                P[node] = cur;
                Q.insert(make_pair(D[node], node));
            }
        }
        visited[cur] = true;
    }
    return D[goal];
}

// DFS
const int dfs_max_sz = 100000;
bitset<dfs_max_sz> visited;

void dfs(ll u){
    if (visited[u]) continue;
    visited[u] = true;
    trav(v, G[u]) dfs(v);

}

// BFS
const int bfs_max_sz = 100000;
vi D(bfs_max_sz, -1);
queue<ll> Q;
Q.push(0);
D[0] = 0;

while (!Q.empty()){
    ll u = Q.front();
    Q.pop();
    trav(v, G[u]){
        if (D[v] == -1){
            D[v] = D[u] + 1;
            Q.push(v);
        }
    }
}

// FLOW GRAPHS

// Ford-Fulkerson's

class FordFulkerson {
private:
    int n, source, sink;
    vvi cap, initialCap;
    vector<bool> seen;
    int dfs(int v, int amount) {
        if (v == sink)
            return amount;
        seen[v] = true;
        rep(u, 0, n) {
            if (cap[v][u] > 0 && !seen[u]) {
                int sent = dfs(u, min(amount, cap[v][u]));
                if (sent > 0) {
                    cap[v][u] -= sent;
                    cap[u][v] += sent;
                    return sent;
                }
            }
        }
        return 0;
    }
    int maximum_flow() {
        int total = 0;
        int sent = -1;
        while (sent != 0) {
            seen = vector<bool> (n, false);
            sent = dfs(source, INF);
            total += sent;
        }
        return total;
    }

public:
    void cin_edges(int numNodes, int m) {
        n = numNodes;
        cap = vvi (n, vi (n, 0));
        rep(i, 0, m) {
            ll v, u, c;
            cin >> v >> u >> c;
            cap[v][u] += c;
        }
        source = n-2, sink = n-1;
        initialCap = cap;
    }
    void copy_matrix(vvi matrix) {
        n = matrix.size();
        initialCap = cap = matrix;
        source = n-2, sink = n-1;
    }
    int get_max_flow() {
        return maximum_flow();
    }
    vvi get_edges() {
        vvi edges;
        rep(v, 0, n) rep(u, 0, n)
                if (cap[v][u] < initialCap[v][u])
                    edges.pb({v, u, initialCap[v][u] - cap[v][u]});
        return edges;
    }
    vvi get_cap() {
        return cap;
    }
};

void test_ford_fulkerson() {
    cin.sync_with_stdio(0); cin.tie(0);
	cin.exceptions(cin.failbit);
    FordFulkerson solver;
    vvi adj_matrix = {
        //012345
        { 0,4,0,0,0,0 }, 
        { 0,0,2,0,0,3 },
        { 0,0,0,3,0,0 },
        { 0,0,0,0,0,2 },
        { 5,0,3,0,0,0 },
        { 0,0,0,0,0,0 }
    };
    solver.copy_matrix(adj_matrix);
    vvi cap = solver.get_paths();
    trav(node, cap){
        trav(adj, node) {
            cout << adj << ' ';
        }
        cout << endl;
    }
    cout << (solver.get_max_flow()) << endl;
    vvi edges = solver.get_paths();
    trav(edge, edges) {
        trav(x, edge) {
            cout << x << ' ';
        }
        cout << endl;
    }
}
