#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;


pair<int, int> req[200000], bus[200000];


int main() {
	int N, M;
	cin >> N >> M;
	assert(1 <= N <= 200000 && 1 <= M <= 200000);
	for (int i = 0; i < N; i++) {
		cin >> req[i].first >> req[i].second;
	}
	for (int i = 0; i < M; i++) {
		cin >> bus[i].first >> bus[i].second;
	}
	sort(req, req + N);
	sort(bus, bus + M);
	int i = 0;
	int j = 0;
	int ans = 0;
	while (i < N && j < M) {
		if (req[i].first > bus[j].first) {
			j++;
			continue;
		}
		if (req[i].second < bus[j].second) {
			i++;
			continue;
		}
		ans++;
		cout << req[i].first << ' ' << req[i].second << ' ' << bus[j].first << ' ' << bus[j].second << '\n';
		i++;
		j++;
	}
	cout << ans;
}
