#include <iostream>
using namespace std;

int N;
int* total;

int calc(int n) {
	if (total[n] != -1) {
		return total[n];
	}
	int cur = (calc(n - 1) + calc(n - 2)) % 15746;
	total[n] = cur;
	return cur;
}

int main() {
	cin >> N;
	total = new int[N + 1];
	total[1] = 1;
	total[2] = 2;
	for (int i = 3; i < N + 1; i++) {
		total[i] = -1;
	}
	cout << calc(N);
}
