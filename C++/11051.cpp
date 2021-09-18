#include <iostream>
#include <cmath>
using namespace std;

long long C(long long n, long long r);

long long** all;

int main() {
	all = new long long*[1001];
	for (int i = 0; i < 1001; i++) {
		all[i] = new long long[1001];
		for (int j = 0; j < 1001; j++) {
			all[i][j] = -1;
		}
	}
	int N, K;
	cin >> N >> K;
	cout << C(N, K);
}

long long C(long long n, long long r)
{
	if (n == r || r == 0)
		return 1;
	if (all[n][r] != -1)
		return all[n][r];
	long long tmp = (C(n - 1, r - 1) + C(n - 1, r)) % 10007;
	all[n][r] = tmp;
	return tmp;
}
