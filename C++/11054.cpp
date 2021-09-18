#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int* A = new int[N];
	int* inc = new int[N];
	int* dec = new int[N];
	for (int i = 0; i < N; i++) {
		cin >> A[i];
		inc[i] = 1;
		dec[i] = 0;
		for (int j = 0; j < i; j++) {
			if (A[i] > A[j] && inc[j] + 1 > inc[i])
				inc[i] = inc[j] + 1;
		}
	}
	for (int i = N - 1; i >= 0; i--) {
		for (int j = N - 1; j > i; j--) {
			if (A[i] > A[j] && dec[j] + 1 > dec[i])
				dec[i] = dec[j] + 1;
		}
	}
	int max = 0;
	for (int i = 0; i < N; i++) {
		if (inc[i] + dec[i] > max) {
			max = inc[i] + dec[i];
		}
	}
	cout << max;
}
