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


struct RandomSet {
    map<int, int> dict;
    int *arr;
    int arr_sz = 0;
    int max_sz;

    RandomSet(int max_sz) {
        arr = new int[max_sz];
    }

    void add(int el) {
        dict[el] = arr_sz;
        arr[arr_sz++] = el;
    }

    void remove(int el) {
        int index = dict[el];
        if (index == --arr_sz)
            return;
        arr[index] = arr[arr_sz];
        dict[arr[index]] = index;
    }

    int get_random() {
        int idx = rand() % arr_sz;
        return arr[idx];
    }
};

int get_closest(int cur, int *points_arr, int arr_sz, int x[], int y[]) {
    int closest = -1;
    int d = INF;
    for (auto it = points_arr, end = points_arr + arr_sz; it < end; it++) {
        int d2 = abs(x[cur] - x[*it]) + abs(y[cur] - y[*it]);
        if (d2 < d) {
            closest = *it;
            d = d2;
        }
    }
    return closest;
}

int get_start(int N, int x[], int y[]) {
    vvi points(N);
    rep(i, 0, N) {
        points[i] = {x[i], y[i], i};
    }
    sort(points.begin(), points.end());
    return points[N/2][2];
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
    deque<int> best_path;
    int min_path_len = INF;
    
    int num_tries[11] = {10, 1, 1, 10, 40, 200, 800, 50, 10, 1, 1};
    int seeds[11] = {0, 0, 1000, 100, 100, 1000, 1000, 1000, 1000, 1000, 1000};
    
    srand(seeds[T]);
    //int same_start = get_start(N, x, y);

    RandomSet starting_points(N);
    rep(i, 0, N) {
        starting_points.add(i);
    }

    for (int try_num = 0, stop1 = min(num_tries[T], N); try_num < stop1; try_num++) {
        RandomSet points(N);
        rep(i, 0, N) {
            points.add(i);
        }
        int start = starting_points.get_random();
        starting_points.remove(start);
        points.remove(start);

        deque<int> path;
        path.emplace_front(start);
        int p_len = 0;

        int tail = start, head = start; 
        bool at_head = true;
        int tail_choice = -1, head_choice = -1;
        int tail_d = INF, head_d = INF;


        for (int i = 0, stop2 = N/2 - 1; i < stop2; i++) {
            if (head_choice == -1) {
                head_choice = get_closest(head, points.arr, points.arr_sz, x, y);
                head_d = abs(x[head] - x[head_choice]) + abs(y[head] - y[head_choice]);
            }
            if (i > 0 && tail_choice == -1) {
                tail_choice = get_closest(tail, points.arr, points.arr_sz, x, y);
                tail_d = abs(x[tail] - x[tail_choice]) + abs(y[tail] - y[tail_choice]);
            }
            if (head_d < tail_d) {
                points.remove(head_choice);
                p_len += abs(x[head] - x[head_choice]) + abs(y[head] - y[head_choice]);
                head = head_choice;
                head_choice = -1;
                path.emplace_front(head);
                if (head == tail_choice) {
                    tail_choice = -1;
                }
            } else {
                points.remove(tail_choice);
                p_len += abs(x[tail] - x[tail_choice]) + abs(y[tail] - y[tail_choice]);
                tail = tail_choice;
                tail_choice = -1;
                path.emplace_back(tail);
                if (tail == head_choice) {
                    head_choice = -1;
                }
            }
        }
        //cout << endl;
        if (p_len < min_path_len) {
            best_path.clear();
            trav(it, path) {
                best_path.emplace_front(it);
            }
                
            min_path_len = p_len;
        }

    }
    trav(it, best_path) {
        cout << it + 1 << " ";
    }
    cout << endl;
}
