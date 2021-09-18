#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N, num;
	string op;
	stack<int> s;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> op;
		if (op == "push") {
			cin >> num;
			s.push(num);
		}
		else if (op == "size")
			cout << s.size() << '\n';
		else if (op == "empty")
			cout << s.empty() << '\n';
		else if (s.empty())
			cout << -1 << '\n';
		else {
			cout << s.top() << '\n';
			if (op == "pop")
				s.pop();
		}
	}
}
