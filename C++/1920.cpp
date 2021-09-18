#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	int N, M;
	cin >> N;
	int* num = new int[N];
	for (int i = 0; i < N; i++)
		cin >> num[i];
	sort(num, num + N);
	cin >> M;
	int cur, left, mid, right;
	for (int i = 0; i < M; i++) {
		cin >> cur;
		left = 0;
		right = N - 1;
		while (left != right) {
			mid = (left + right) / 2;
			if (num[mid] < cur)
				left = mid + 1;
			else
				right = mid;
		}
		if (num[left] == cur)
			cout << 1 << "\n";
		else
			cout << 0 << "\n";
	}
}
