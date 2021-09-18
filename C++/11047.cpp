#include <iostream>
using namespace std;

int main() {
	int N, K;
	cin >> N >> K;
	int* A = new int[N];
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	int counter = 0;
	for (int i = N - 1; i >= 0; i--) {
		while (A[i] <= K) {
			K -= A[i];
			counter++;
		}
	}
	cout << counter;
}
