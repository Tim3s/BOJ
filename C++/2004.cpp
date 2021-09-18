#include <iostream>
using namespace std;

int main() {
	long long n, m, sub, two(0), twodiv(2), five(0), fivediv(5);
	cin >> n >> m;
	sub = n - m;
	for (int i = 0; twodiv <= n; i++) {
		two += n / twodiv - m / twodiv - sub / twodiv;
		twodiv *= 2;
		five += n / fivediv - m / fivediv - sub / fivediv;
		fivediv *= 5;
	}
	cout << min(two, five);
}
