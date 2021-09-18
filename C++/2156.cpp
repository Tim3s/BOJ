#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int* cur1 = new int[2];
	int* cur2 = new int[2];
	int* cur3 = new int[2];
	int* next;
	cin >> cur1[1];
	if (N == 1) {
		cout << cur1[1];
		return 0;
	}
	cur1[0] = 0;
	cin >> cur2[1];
	cur2[0] = cur1[1] + cur2[1];
	if (N == 2) {
		cout << cur2[0];
		return 0;
	}
	cin >> cur3[1];
	cur3[0] = cur2[1] + cur3[1];
	cur3[1] += cur1[1];
	int tmp;
	for (int i = 3; i < N; i++) {
		cin >> tmp;
		next = new int[2];
		next[0] = cur3[1] + tmp;
		next[1] = max(max(cur1[0], cur1[1]), max(cur2[0], cur2[1])) + tmp;
		cur1 = cur2;
		cur2 = cur3;
		cur3 = next;
	}
	cout << max(max(cur2[0], cur2[1]), max(cur3[0], cur3[1]));
}
