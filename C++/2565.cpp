#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int* A = new int[501];
	int* length = new int[501];
	int loc;
	for (int i = 1; i < 501; i++) {
		A[i] = -1;
		length[i] = 1;
	}
	for (int i = 0; i < N; i++) {
		cin >> loc;
		cin >> A[loc];
	}
	for (int i = 1; i < 501; i++) {
		if (A[i] != -1) {
			for (int j = 1; j < i; j++) {
				if (A[j] != -1 && A[i] > A[j] && length[j] + 1 > length[i])
					length[i] = length[j] + 1;
			}
		}
	}
	int max = 0;
	for (int i = 1; i < 501; i++) {
		if (length[i] > max) {
			max = length[i];
		}
	}
	cout << N - max;
}
