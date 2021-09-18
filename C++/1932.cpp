#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	int* cur = new int[1];
	int* next;
	cin >> cur[0];
	int tmp;
	for (int i = 2; i <= n; i++) {
		next = new int[i];
		for (int j = 0; j < i; j++) {
			cin >> tmp;
			if (j == 0)
				next[0] = cur[0] + tmp;
			else if (j == i - 1)
				next[j] = cur[j - 1] + tmp;
			else
				next[j] = max(cur[j - 1], cur[j]) + tmp;
		}
		cur = next;
	}
	tmp = cur[0];
	for (int i = 1; i < n; i++) {
		if (cur[i] > tmp)
			tmp = cur[i];
	}
	cout << tmp;
}
