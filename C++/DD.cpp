#include <iostream>
#include <vector>
#include <cmath>
#include <climits>
#include <cstring>
using namespace std;
#define ll long long


ll tree[200001];
int segment[524288], N, A[200001], i, j, K;


void update(int x, int val) {
	while (x <= K) {
		tree[x] += val;
		x += x & -x;
	}
}


ll getsum(int x) {
	ll res = 0;
	while (x > 0) {
		res += tree[x];
		x -= x & -x;
	}
	return res;
}


int init(int left, int right, int idx) {
	if (left == right) {
		segment[idx] = A[left];
		return segment[idx];
	}
	int mid = (left + right) >> 1;
	idx <<= 1;
	return segment[idx] = min(init(left, mid, idx), init(mid + 1, right, idx + 1));
}


int updateseg(int left, int right, int idx) {
	if (i < left || i > right) {
		return segment[idx];
	}
	if (left == right) {
		return segment[idx] = j;
	}
	int mid = (left + right) >> 1;
	idx <<= 1;
	return segment[idx] = min(updateseg(left, mid, idx), updateseg(mid + 1, right, idx + 1));
}


int getl(int left, int right, int idx) {
	if (segment[idx] >= j) {
		return 0;
	}
	if (left == right) {
		return (left <= i ? left : 0);
	}
	int mid = (left + right) >> 1;
	idx <<= 1;
	if (mid >= i) {
		return getl(left, mid, idx);
	}
	return max(getl(left, mid, idx), getl(mid + 1, right, idx + 1));
}


int getr(int left, int right, int idx) {
	if (segment[idx] >= j) {
		return K;
	}
	if (left == right) {
		return (left >= i ? left : K);
	}
	int mid = (left + right) >> 1;
	idx <<= 1;
	if (mid < i) {
		return getr(mid + 1, right, idx + 1);
	}
	return min(getr(left, mid, idx), getr(mid + 1, right, idx + 1));
}


int main() {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);
	cin >> N;
	K = N + 1;
	for (int k = 1; k <= N; k++) {
		cin >> A[k];
		update(k, A[k]);
	}
	init(1, N, 1);
	int M, q;
	cin >> M;
	while (M--) {
		cin >> q >> i >> j;
		if (q == 1) {
			update(i, j - A[i]);
			A[i] = j;
			updateseg(1, N, 1);
			continue;
		}
		int l = getl(1, N, 1);
		int r = getr(1, N, 1) - 1;
		cout << getsum(r) - getsum(l) << '\n';
	}
}
