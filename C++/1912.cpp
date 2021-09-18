#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;
	int* sums = new int[n];
	int tmp;
	cin >> sums[0];
	for (int i = 1; i < n; i++) {
		cin >> tmp;
		sums[i] = max(sums[i - 1], 0) + tmp;
	}
	cout << *max_element(sums, sums + n);
}
