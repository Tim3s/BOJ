#include <iostream>
#include <algorithm>
using namespace std;

int conquer[37250], last[37250];

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	int N;
	cin >> N;
	int V, E;
	for (int i = 1; i <= N; i++) {
		cin >> V >> E;
		conquer[i] = V - E;
		last[i] = last[i - 1] + V;
		for (int j = 0; j < E; j++) {
			cin >> V >> V;
		}
	}
	int Q;
	cin >> Q;
	int t, u, v;
	for (int i = 0; i < Q; i++) {
		cin >> t >> u;
		if (t == 1) {
			cout << conquer[u] << '\n';
			continue;
		}
		cin >> v;
		v = lower_bound(last, last + N, u) - last;
		if (t == 2)
			conquer[v]++;
		else
			conquer[v]--;
	}
}
