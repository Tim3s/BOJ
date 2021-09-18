#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int N, M;
int p[100001], x[100000];


int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> p[i];
	}
	for (int i = 0; i < N; i++) {
		cin >> x[i];
	}
	int cur = 0;
	int nxt = 1;
	int ans = 0;
	while (true) {
		if (p[cur] + x[cur] >= M) {
			cout << ans;
			return 0;
		}
		pair<int, int> nxt2 = {p[cur] + x[cur], 0};
		while (p[cur] + x[cur] >= p[nxt] && nxt < N) {
			nxt2 = max(nxt2, { p[nxt] + x[nxt], nxt });
			nxt++;
		}
		if (nxt2.second == 0) {
			cout << -1;
			return 0;
		}
		cur = nxt2.second;
		ans++;
	}
}
