#include <iostream>
#include <string>
#include <deque>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N, num;
	string op;
	deque<int> d;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> op;
		if (op == "push_front") {
			cin >> num;
			d.push_front(num);
		}
		else if (op == "push_back") {
			cin >> num;
			d.push_back(num);
		}
		else if (op == "size")
			cout << d.size() << '\n';
		else if (op == "empty")
			cout << d.empty() << '\n';
		else if (d.empty())
			cout << -1 << '\n';
		else if (op[op.length() - 1] == 'k') {
			cout << d.back() << '\n';
			if (op[0] == 'p')
				d.pop_back();
		}
		else {
			cout << d.front() << '\n';
			if (op[0] == 'p')
				d.pop_front();
		}
	}
}
