#include <iostream>
using namespace std;

long long* total;

long long calc(int n) {
	if (total[n] != -1) {
		return total[n];
	}
	long long cur = calc(n - 1) + calc(n - 5);
	total[n] = cur;
	return cur;
}

int main() {
	total = new long long[101];
	total[1] = 1;
	total[2] = 1;
	total[3] = 1;
	total[4] = 2;
	total[5] = 2;
	for (int i = 6; i < 101; i++) {
		total[i] = -1;
	}
	int T, N;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		cout << calc(N) << endl;
	}
}
