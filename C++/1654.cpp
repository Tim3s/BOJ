#include <iostream>
#include <numeric>
using namespace std;

int main() {
	int K, N;
	cin >> K >> N;
	long long* all = new long long[K];
	long long right(0);
	for (int i = 0; i < K; i++) {
		cin >> all[i];
		right = max(right, all[i]);
	}
	int n;
	long long left = 1, mid, max(0);
	while (left <= right) {
		mid = (left + right) / 2;
		n = 0;
		for (int i = 0; i < K; i++)
			n += all[i] / mid;
		if (n >= N) {
			if (mid > max)
				max = mid;
			left = mid + 1;
		}
		else
			right = mid - 1;
	}
	cout << max;
}
