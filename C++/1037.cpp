#include <iostream>
#include <algorithm>
using namespace std;

long long gcd(long long a, long long b);
long long lcm(long long a, long long b);

int main() {
	int N;
	cin >> N;
	long long res(1);
	long long* num = new long long[N];
	for (int i = 0; i < N; i++)
		cin >> num[i];
	if (N == 1) {
		cout << num[0] * num[0];
		return 0;
	}
	sort(num, num + N);
	for (int i = 0; i < N; i++) {
		if (res % num[i] != 0)
			res = lcm(res, num[i]);
	}
	if (num[N - 1] == res)
		res *= num[0];
	cout << res;
}

long long gcd(long long a, long long b)
{
	long long tmp;
	if (a < b) {
		tmp = b;
		b = a;
		a = tmp;
	}
	while (a != b) {
		tmp = a - b;
		a = max(b, tmp);
		b = min(b, tmp);
	}
	return b;
}

long long lcm(long long a, long long b)
{
	return (a * b) / gcd(a, b);
}
