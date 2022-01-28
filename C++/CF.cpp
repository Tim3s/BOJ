#include<iostream>
#include<cmath>
using namespace std;

bool notprime[200000];
int prime[120053] = { 2, };
int t;
int n;
int a[200001];

int main() {
	int idx = 1;
	for (int i = 3; i < 200000; i += 2) {
		if (!notprime[i]) {
			prime[idx] = i;
			idx++;
			for (int j = i * 3; j < 200000; j += i << 1) {
				notprime[j] = true;
			}
		}
	}
	int** has = new int* [200001];
	for (int i = 0; i < 200001; i++) {
		has[i] = new int[120053];
	}
	cin >> t;
	while (t--) {
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}
		a[n] = a[0];
		for (int i = 0; i < n; i++) {

		}
	}
}
