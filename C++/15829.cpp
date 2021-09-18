#include <iostream>
using namespace std;

long long calc(int a, int b);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int L;
	long long res = 0;
	char t;
	cin >> L;
	for (int i = 0; i < L; i++) {
		cin >> t;
		res += ((t - 'a' + 1) * calc(31, i)) % 1234567891;
		res = res % 1234567891;
	}
	cout << res % 1234567891;
}

long long calc(int a, int b)
{
	long long res = 1;
	for (int i = 0; i < b; i++) {
		res *= a;
		res = res % 1234567891;
	}
	return res;
}
