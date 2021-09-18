#include <iostream>
#include <string.h>
using namespace std;

int memo[3000][3000][2][2], num[3000];


int dp(int left, int right, int odd, int turn) {
	if (left > right)
		return 1 - (odd ^ turn);
	if (memo[left][right][odd][turn] != -1)
		return memo[left][right][odd][turn];
	memo[left][right][odd][turn] = 0;
	if (turn) {
		if (!dp(left, right - 1, odd, 0) || !dp(left + 1, right, odd, 0))
			return memo[left][right][odd][turn] = 1;
		if (left < right && (!dp(left, right - 2, odd, 0) || !dp(left + 2, right, odd, 0)))
			return memo[left][right][odd][turn] = 1;
		return 0;
	}
	if (!dp(left, right - 1, odd ^ num[right], 1) || !dp(left + 1, right, odd ^ num[left], 1))
		return memo[left][right][odd][turn] = 1;
	if (left < right && (!dp(left, right - 2, odd ^ num[right] ^ num[right - 1], 1) || !dp(left + 2, right, odd ^ num[left] ^ num[left + 1], 1)))
		return memo[left][right][odd][turn] = 1;
	return 0;
}


int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> num[i];
		num[i] %= 2;
	}
	memset(memo, -1, sizeof(memo));
	cout << (dp(0, N - 1, 0, 0) ? "Yes" : "No");
}
