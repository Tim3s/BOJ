#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int* cur1 = new int[2];
	int* cur2 = new int[2];
	int* next;
	cin >> cur1[1];
	cin >> cur2[1];
	cur2[0] = cur1[1] + cur2[1];
	int tmp;
	for (int i = 2; i < N; i++) {
		cin >> tmp;
		next = new int[2];
		next[0] = cur2[1] + tmp;
		next[1] = max(cur1[0], cur1[1]) + tmp;
		cur1 = cur2;
		cur2 = next;
	}
	cout << max(cur2[0], cur2[1]);
}
