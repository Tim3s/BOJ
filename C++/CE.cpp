#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;

int q, n, k;
int a[300000], t[300000];
int res[300000];
pair<int, int> inc[300000];

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> q;
	while (q--) {
		cin >> n >> k;
		for (int i = 0; i < n; i++)
			res[i] = 2000000000;
		for (int i = 0; i < k; i++) {
			cin >> a[i];
			a[i]--;
		}
		for (int i = 0; i < k; i++) {
			cin >> t[i];
			res[a[i]] = t[i];
			inc[i].first = t[i];
			inc[i].second = i;
		}
		sort(inc, inc + k);
		for (int i = 0; i < k; i++) {
			int idx = inc[i].second;
			int tmp = inc[i].first + 1;
			int loc = a[idx];
			for (int j = 1; j < max(loc + 1, n - loc); j++) {
				bool done = false;
				if (j < n - loc && res[loc + j] > tmp) {
					res[loc + j] = tmp;
					done = true;
				}
				if (j <= loc && res[loc - j] > tmp) {
					res[loc - j] = tmp;
					done = true;
				}
				tmp++;
				if (!done) {
					break;
				}
			}
		}
		for (int i = 0; i < n; i++) {
			cout << res[i] << ' ';
		}
		cout << '\n';
	}
}
