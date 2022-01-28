#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int weeks[20001];
int X[20001], cancount[20001];
bool cant[20001][20001];

int main() {
	int N, M;
	cin >> N >> M;
	int lcm = N;
	while (lcm % M != 0) {
		lcm += N;
	}
	for (int i = 1; i <= N; i++) {
		cin >> X[i];
		cancount[i] = lcm / N;
	}
	for (int i = M - 1; i <= lcm; i += M) {
		cant[i % N + 1][i / N + 1] = true;
		cancount[i % N + 1]--;
	}
	for (int i = 1; i <= N; i++) {
		if (cancount[i] == 0) {
			weeks[i] = INT_MAX;
			continue;
		}
		weeks[i] = (X[i] / cancount[i]) * (lcm / N);
		if (X[i] % cancount[i] == 0) {
			int cur = lcm / N;
			while (cant[i][cur]) {
				cur--;
				weeks[i]--;
			}
		}
		else {
			int cur = 0;
			int tmp = X[i] % cancount[i];
			while (tmp) {
				cur++;
				weeks[i]++;
				if (!cant[i][cur]) {
					tmp--;
				}
			}
		}
	}
	int idx = 1;
	for (int i = 2; i <= N; i++) {
		if (weeks[idx] > weeks[i]) {
			idx = i;
		}
	}
	cout << idx;
}
