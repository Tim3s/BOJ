#include <iostream>
using namespace std;

int main() {
	int N, right = 0;
	long long M;
	cin >> N >> M;
	long long* tree = new long long[N] ;
	for (int i = 0; i < N; i++) {
		cin >> tree[i];
		if (tree[i] > right)
			right = tree[i];
	}
	long long hsum;
	long long result = 0;
	long long left = 0;
	while (left < right) {
		long long mid = (left + right) / 2;
		hsum = 0;
		for (int i = 0; i < N; i++) {
			hsum += max(0LL, tree[i] - mid);
		}
		if (hsum >= M) {
			left = mid + 1;
			if (result < mid)
				result = mid;
		}
		else
			right = mid;
	}
	cout << result;
}
