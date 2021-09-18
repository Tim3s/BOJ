#include <iostream>
using namespace std;

int factorial(int n);
int C(int n, int r);

int main() {
	int n, r;
	cin >> n >> r;
	cout << C(n, r);
}

int factorial(int n)
{
	if (n == 0 || n == 1)
		return 1;
	return n * factorial(n - 1);
}

int C(int n, int r)
{
	return factorial(n) / factorial(r) / factorial(n - r);
}
