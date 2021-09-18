#include <iostream>
using namespace std;

int main() {
	int loopn;
	cin >> loopn;
	int* cur = new int[3];
	int* next = new int[3];
	int tmp;
	for (int i = 0; i < 3; i++) {
		cin >> cur[i];
	}
	for (int i = 1; i < loopn; i++) {
		for (int j = 0; j < 3; j++) {
			cin >> tmp;
			next[j] = min(cur[(j + 1) % 3] + tmp, cur[(j + 2) % 3] + tmp);
		}
		for (int j = 0; j < 3; j++)
			cur[j] = next[j];
	}
	cout << min(cur[0], min(cur[1], cur[2]));
}
