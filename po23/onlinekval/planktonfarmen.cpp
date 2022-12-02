#include <bits/stdc++.h>

int main() {
    int A, n;
    std::scanf("%d %d", &A, &n);
    int lengths[n];
    for (int i = 0; i < n; i++)
        std::scanf("%d", &lengths[i]);
    std::sort(lengths, lengths + n);
    int *first = lengths, *last = lengths + n - 1;
    while (first < last) {
        if (*first * *last >= A)
            last--;
        first++;
    }
    std::cout << (lengths + n -1) - last << std::endl;
}