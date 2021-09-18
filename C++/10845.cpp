#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N, num;
	string op;
	queue<int> q;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> op;
		if (op == "push") {
			cin >> num;
			q.push(num);
		}
		else if (op == "size")
			cout << q.size() << '\n';
		else if (op == "empty")
			cout << q.empty() << '\n';
		else if (q.empty())
			cout << -1 << '\n';
		else if (op == "back")
			cout << q.back() << '\n';
		else {
			cout << q.front() << '\n';
			if (op == "pop")
				q.pop();
		}
	}
}
