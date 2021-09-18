#include <iostream>
using namespace std;

int C(int n, int r);

int** clist;

int main() {
	clist = new int* [30];
	for (int i = 1; i < 30; i++) {
		clist[i] = new int[i + 1];
		for (int j = 0; j <= i; j++) {
			if (i == j || j == 0)
				clist[i][j] = 1;
			else
				clist[i][j] = -1;
		}
	}
	int T, N, M;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N >> M;
		cout << C(M, N) << '\n';
	}
}

int C(int n, int r) {
	if (clist[n][r] != -1)
		return clist[n][r];
	int tmp = C(n - 1, r - 1) + C(n - 1, r);
	clist[n][r] = tmp;
	return tmp;
}
