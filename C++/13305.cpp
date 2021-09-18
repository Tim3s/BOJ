#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	long long* len = new long long[N - 1];
	for (int i = 0; i < N - 1; i++)
		cin >> len[i];
	long long* oil = new long long[N];
	for (int i = 0; i < N; i++)
		cin >> oil[i];
	long long price = oil[0];
	long long total = 0;
	for (int i = 0; i < N - 1; i++) {
		total += price * len[i];
		price = min(price, oil[i + 1]);
	}
	cout << total;
}
