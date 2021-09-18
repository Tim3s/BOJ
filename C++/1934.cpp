#include <iostream>
using namespace std;

long long gcd(long long a, long long b);
long long lcm(long long a, long long b);

int main() {
	int T, A, B;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> A >> B;
		cout << lcm(A, B) << '\n';
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

long long lcm(long long a, long long b)
{
	return (a * b) / gcd(a, b);
}
