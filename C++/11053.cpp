#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int* A = new int[N];
	int* length = new int[N];
	for (int i = 0; i < N; i++) {
		cin >> A[i];
		length[i] = 1;
		for (int j = 0; j < i; j++) {
			if (A[i] > A[j] && length[j] + 1 > length[i])
				length[i] = length[j] + 1;
		}
	}
	int max = 0;
	for (int i = 0; i < N; i++) {
		if (length[i] > max) {
			max = length[i];
		}
	}
	cout << max;
}
