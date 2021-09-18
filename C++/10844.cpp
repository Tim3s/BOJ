#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	long long* cur = new long long[10];
	cur[0] = 0;
	for (int i = 1; i < 10; i++)
		cur[i] = 1;
	long long* next;
	for (int i = 1; i < N; i++) {
		next = new long long[10];
		next[0] = cur[1];
		for (int j = 1; j < 9; j++)
			next[j] = (cur[j - 1] + cur[j + 1]) % 1000000000;
		next[9] = cur[8];
		cur = next;
	}
	long long tmp = 0;
	for (int i = 0; i < 10; i++) {
		tmp = (tmp + cur[i]) % 1000000000;
	}
	cout << tmp;
}
