#include <iostream>
#include <string>
#include <stack>
using namespace std;

bool check(string t);

int main() {
	cin.tie(NULL);
	string text;
	getline(cin, text);
	while (text != ".") {
		if (check(text))
			cout << "yes\n";
		else
			cout << "no\n";
		getline(cin, text);
	}
}

bool check(string t)
{
	stack<char> s;
	for (int i = 0; i < t.length(); i++) {
		if (t[i] == '(' || t[i] == '[')
			s.push(t[i]);
		else if (t[i] == ')' || t[i] == ']') {
			if (s.empty() || (t[i] == ')' && s.top() == '[') || (t[i] == ']' && s.top() == '('))
				return false;
			s.pop();
		}
	}
	if (s.empty())
		return true;
	return false;
}
