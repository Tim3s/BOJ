#include <iostream>
using namespace std;

int nxt[1000001], prv[1000001];

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	int N, M;
	cin >> N >> M;
	int* initial = new int[N];
	cin >> initial[0];
	for (int i = 1; i < N; i++) {
		cin >> initial[i];
		nxt[initial[i - 1]] = initial[i];
		prv[initial[i]] = initial[i - 1];
	}
	nxt[initial[N - 1]] = initial[0];
	prv[initial[0]] = initial[N - 1];
	char command[2];
	int i, j;
	while (M--) {
		cin >> command[0] >> command[1];
		if (command[0] == 'B') {
			cin >> i >> j;
			if (command[1] == 'N') {
				cout << nxt[i] << '\n';
				prv[nxt[i]] = j;
				nxt[j] = nxt[i];
				nxt[i] = j;
				prv[j] = i;
				continue;
			}
			cout << prv[i] << '\n';
			nxt[prv[i]] = j;
			prv[j] = prv[i];
			prv[i] = j;
			nxt[j] = i;
			continue;
		}
		cin >> i;
		if (command[1] == 'N') {
			cout << nxt[i] << '\n';
			nxt[i] = nxt[nxt[i]];
			prv[nxt[i]] = i;
			continue;
		}
		cout << prv[i] << '\n';
		prv[i] = prv[prv[i]];
		nxt[prv[i]] = i;
	}
}
