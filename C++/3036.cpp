#include <iostream>
using namespace std;

long long gcd(long long a, long long b);

int main() {
	int N, denom, numer, mygcd;
	cin >> N >> numer;
	for (int i = 1; i < N; i++) {
		cin >> denom;
		mygcd = gcd(denom, numer);
		cout << numer / mygcd << '/' << denom / mygcd << '\n';
	}
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
