#include <iostream>

using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;
    
    bool found = false;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        if (a == k) {
            found = true;
        }
    }
    
    if (found) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}

int main() {
    // These two lines make input/output faster for competitive programming
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    
    return 0;
}