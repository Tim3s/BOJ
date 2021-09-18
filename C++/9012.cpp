#include <iostream>
#include <string>
using namespace std;

bool check(string t);

int main() {
	string text;
	int ln;
	cin >> ln;
	cin.ignore();
	for (int i = 0; i < ln; i++) {
		getline(cin, text);
		if (check(text))
			cout << "YES\n";
		else
			cout << "NO\n";
	}
}

bool check(string t) {
	int cnt = 0;
	for (int i = 0; i < t.length(); i++) {
		if (t[i] == '(')
			cnt++;
		else
			cnt--;
		if (cnt < 0)
			return false;
	}
	return cnt == 0;
}
