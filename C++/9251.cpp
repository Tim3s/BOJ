#include <iostream>
#include <string>
using namespace std;

int main() {
	string A, B;
	cin >> A >> B;
	int Alen = A.length();
	int Blen = B.length();
	int** matrix = new int* [Alen];
	for (int i = 0; i < Alen; i++) {
		matrix[i] = new int[Blen];
	}
	if (A[0] == B[0])
		matrix[0][0] = 1;
	else
		matrix[0][0] = 0;
	for (int i = 1; i < Alen; i++) {
		if (A[i] == B[0])
			matrix[i][0] = 1;
		else
			matrix[i][0] = matrix[i - 1][0];
	}
	for (int i = 1; i < Blen; i++) {
		if (A[0] == B[i])
			matrix[0][i] = 1;
		else
			matrix[0][i] = matrix[0][i - 1];
	}
	for (int i = 1; i < Alen; i++) {
		for (int j = 1; j < Blen; j++) {
			if (A[i] != B[j])
				matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1]);
			else
				matrix[i][j] = matrix[i - 1][j - 1] + 1;
		}
	}
	cout << matrix[Alen - 1][Blen - 1];
}
