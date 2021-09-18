#include <iostream>
#include <algorithm>
using namespace std;

long long gcd(long long a, long long b);

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	int N;
	cin >> N;
	long long* num = new long long[N];
	for (int i = 0; i < N; i++)
		cin >> num[i];
	for (int i = 1; i < N; i++)
		num[i - 1] = abs(num[i] - num[i - 1]);
	int mygcd = num[0];
	for (int i = 1; i < N - 1; i++)
		mygcd = gcd(mygcd, num[i]);
	for (int i = 2; i <= mygcd / 2; i++) {
		if (mygcd % i == 0)
			cout << i << ' ';
	}
	cout << mygcd;
}

long long gcd(long long a, long long b)
{
	long long tmp;
	if (a < b) {
		tmp = b;
		b = a;
		a = tmp;
	}
	while (b != 0) {
		tmp = a % b;
		a = b;
		b = tmp;
	}
	return a;
}
