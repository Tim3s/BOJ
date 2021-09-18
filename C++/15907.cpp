#include <iostream>
using namespace std;


int last[2000001];
int cnt[2000001];
int times[1001];


int main() {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);
	int ans = 2;
	int N;
	cin >> N;
	if (N <= 2) {
		cout << N;
		return 0;
	}
	for (int i = 0; i < N; i++) {
		cin >> times[i];
	}
	ans = 0;
	int tmp = max(N / 2 - 1, 1);
	for (int k = 2; k * tmp <= times[N - 1]; k ++) {
		for (int i = 0; i < N; i++) {
			int r = times[i] % k;
			if (last[r] != k) {
				last[r] = k;
				cnt[r] = 1;
			}
			else
				cnt[r]++;
			if (ans < cnt[r])
				ans = cnt[r];
		}
	}
	cout << ans;
}
