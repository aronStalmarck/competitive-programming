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
#define mp make_pairh

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pii;
typedef map<int, int> mii;

const int INF = (int) 1e9;

struct Point {
    int x;
    int y;
    int id;
    Point(int x = 0, int y = 0, int id = 0): x(x), y(y), id(id) {};
};

struct RandomSet {
    map<int, int> dict;
    int *arr;
    int arr_sz = 0;
    int max_sz;

    RandomSet(int max_sz) {
        arr = new int[max_sz];
    }

    void add(int el) {
        if (!dict.count(el)) {
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

    int get_random() {
        int idx = rand() % arr_sz;
        return arr[idx];
    }
};

int distance(Point p1, Point p2) {
    return abs(p1.x - p2.x) + abs(p1.y - p2.y);
}

int get_closest(int cur, RandomSet points, Point points_by_id[]) {
    int closest;
    int d = INF;
    for (auto it = points.arr, end = points.arr + points.arr_sz; it < end; it++) {
        if (distance(points_by_id[cur], points_by_id[*it]) < d) {
            closest = *it;
            d = distance(cur, *it);
        }
    }
    return closest;
}

int main()
{
    cin.sync_with_stdio(0); cin.tie(0);
    cin.exceptions(cin.failbit);

    int T, N;
    cin >> T >> N;
    Point points_by_id[N+1];
    rep(i, 1, N+1) {
        Point p; cin >> p.x >> p.y; p.id = i;
        points_by_id[i] = p;
    }
    int best_path[N/2];
    int min_path_len = INF;
    
    int num_tries[11] = {10, 1, 1, 10, 40, 50, 10, 1, 1, 1, 1};
    rep(try_num, 0, num_tries[T]) {
        RandomSet points(N+1);
        rep(i, 1, N+1) {
            points.add(i);
        }
        //return 0;
        int cur = points.get_random();
        int p_len = 0;    
        points.remove(cur);
        int path[N/2] = {cur}, p_end = 1;

        rep(i, 0, N/2 - 1) {
            int to = get_closest(cur, points, points_by_id);
            points.remove(to);

            p_len += distance(points_by_id[cur], points_by_id[to]);
            cur = to;
            path[p_end++] = cur;
        }

        if (p_len < min_path_len) {
            memcpy(best_path, path, sizeof(best_path));
            min_path_len = p_len;
        }

    }
    rep(i, 0, N/2) {
        cout << best_path[i] << " ";
    }
    cout << endl;
}