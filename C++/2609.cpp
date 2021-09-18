#include <iostream>
using namespace std;

int main() {
	int a, b;
	int tmp;
	cin >> a >> b;
	int big = max(a, b);
	int small = min(a, b);
	while (big != small) {
		tmp = big - small;
		big = max(tmp, small);
		small = min(tmp, small);
	}
	cout << tmp << endl;
	cout << a * b / tmp;
}
