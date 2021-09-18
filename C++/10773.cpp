#include <iostream>
#include <numeric>
using namespace std;

int main() {
	int K;
	cin >> K;
	int index = 0;
	int* num = new int[K];
	for (int i = 0; i < K; i++) {
		cin >> num[index];
		if (num[index] != 0)
			index++;
		else
			index--;
	}
	cout << accumulate(num, num + index, 0);
}
