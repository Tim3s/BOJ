#include <iostream>

int main() {
	int ln;
	std::cin >> ln;
	int fibonacci[41][2] = { 0 };
	fibonacci[0][0] = 1;
	fibonacci[1][1] = 1;
	for (int i = 2; i < 41; i++) {
		fibonacci[i][0] = fibonacci[i - 1][0] + fibonacci[i - 2][0];
		fibonacci[i][1] = fibonacci[i - 1][1] + fibonacci[i - 2][1];
	}
	int N;
	for (int i = 0; i < ln; i++) {
		std::cin >> N;
		std::cout << fibonacci[N][0] << ' ' << fibonacci[N][1] << std::endl;
	}
}
