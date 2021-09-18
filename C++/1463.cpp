#include <iostream>
using namespace std;

int main() {
	int X;
	cin >> X;
	int* cnt = new int[X + 1];
	cnt[1] = 0;
	for (int i = 2; i <= X; i++) {
		if (i % 3 == 0) {
			if (i % 2 == 0)
				cnt[i] = min(cnt[i - 1], min(cnt[i / 3], cnt[i / 2])) + 1;
			else
				cnt[i] = min(cnt[i - 1], cnt[i / 3]) + 1;
		}
		else {
			if (i % 2 == 0)
				cnt[i] = min(cnt[i - 1], cnt[i / 2]) + 1;
			else
				cnt[i] = cnt[i - 1] + 1;
		}
	}
	cout << cnt[X];
}
