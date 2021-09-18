#include <iostream>
#include <string>
using namespace std;

int main() {
	string cur;
	while (true) {
		cin >> cur;
		if (cur == "0")
			break;
		bool flag = true;
		for (int i = 0; i <= cur.length() / 2; i++) {
			if (cur[i] != cur[cur.length() - i - 1]) {
				flag = false;
				cout << "no" << endl;
				break;
			}
		}
		if (flag)
			cout << "yes" << endl;
	}
}
