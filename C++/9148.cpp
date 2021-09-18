#include <iostream>

int w(int a, int b, int c, int***& wl);

int main() {
	int*** wlist = new int**[21];
	for (int i = 0; i < 21; i++) {
		wlist[i] = new int* [21];
		for (int j = 0; j < 21; j++) {
			wlist[i][j] = new int[21];
			for (int k = 0; k < 21; k++) {
				wlist[i][j][k] = 0;
			}
		}
	}
	int a, b, c;
	while (true) {
		std::cin >> a >> b >> c;
		if (a == -1 && b == -1 && c == -1)
			break;
		std::cout << "w(" << a << ", " << b << ", " << c << ") = " << w(a, b, c, wlist) << std::endl;
	}
}

int w(int a, int b, int c, int***& wl) {
	if (a <= 0 || b <= 0 || c <= 0)
		return 1;
	if (a > 20 || b > 20 || c > 20)
		return w(20, 20, 20, wl);
	if (wl[a][b][c] != 0)
		return wl[a][b][c];
	if (a < b && b < c) {
		int num = w(a, b, c - 1, wl) + w(a, b - 1, c - 1, wl) - w(a, b - 1, c, wl);
		wl[a][b][c] = num;
		return num;
	}
	int num =  w(a - 1, b, c, wl) + w(a - 1, b - 1, c, wl) + w(a - 1, b, c - 1, wl) - w(a - 1, b - 1, c - 1, wl);
	wl [a] [b] [c] = num;
	return num;
}
