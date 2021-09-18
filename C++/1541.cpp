#include <iostream>
#include <string>
using namespace std;

int main() {
	string equ;
	getline(cin, equ);
	int res = 0;
	bool add = true;
	int tmp = 0;
	for (int i = 0; i < equ.length(); i++) {
		if (equ[i] == '+' || equ[i] == '-') {
			if (add)
				res += tmp;
			else
				res -= tmp;
			tmp = 0;

			if (equ[i] == '-')
				add = false;
		}
		else
			tmp = 10 * tmp + equ[i] - '0';
		if (i == equ.length() - 1) {
			if (equ[i] == '-')
				add = false;
			if (add)
				res += tmp;
			else
				res -= tmp;
		}
	}
	cout << res;
}
