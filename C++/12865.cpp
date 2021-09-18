#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N, K;
	cin >> N >> K;
	int* Vsum = new int[K + 1];
	for (int i = 0; i <= K; i++)
		Vsum[i] = 0;
	int W, V;
	for (int i = 0; i < N; i++) {
		cin >> W >> V;
		for (int j = K - 1; j >= 0; j--) {
			if (j + W <= K && Vsum[j + W] < Vsum[j] + V)
				Vsum[j + W] = Vsum[j] + V;
		}
		for (int j = 0; j < K + 1; j++) {
		}
	}
	cout << Vsum[K];
}
