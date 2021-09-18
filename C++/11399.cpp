#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
	int N;
	cin >> N;
	int* P = new int[N];
	for (int i = 0; i < N; i++)
		cin >> P[i];
	sort(P, P + N);
	for (int i = 1; i < N; i++)
		P[i] += P[i - 1];
	cout << accumulate(P, P + N, 0);
}
