#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


long long N, M, X, L, R;
long long *Q, *segment;
long long addon[1000000][3];
vector<long long> quest;


long long update(long long left, long long right, int idx) {
	if (left > X || right < X) {
		return segment[idx];
	}
	if (left == right) {
		return segment[idx] = 1;
	}
	long long mid = (left + right) / 2;
		return segment[idx] = update(left, mid, 2 * idx) + update(mid + 1, right, 2 * idx + 1);
}


long long getsum(long long left, long long right, int idx) {
	if (L > right || R < left)
		return 0;
	if (L <= left && R >= right)
		return segment[idx];
	long long mid = (left + right) / 2;
	return getsum(left, mid, idx * 2) + getsum(mid + 1, right, idx * 2 + 1);
}


int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> N;
	Q = new long long[N];
	for (long long i = 0; i < N; i++) {
		cin >> Q[i];
		quest.push_back(Q[i]);
	}
	cin >> M;
	for (long long i = 0; i < M; i++) {
		cin >> addon[i][0] >> addon[i][1];
		if (addon[i][0] == 1) {
			quest.push_back(addon[i][1]);
		}
		else {
			cin >> addon[i][2];
		}
	}
	sort(quest.begin(), quest.end());
	//quest.erase(unique(quest.begin(), quest.end()), quest.end());
	segment = new long long[quest.size() * 4];
	for (int i = 0; i < quest.size() * 4; i++) {
		segment[i] = 0;
	}
	for (long long i = 0; i < N; i++) {
		X = lower_bound(quest.begin(), quest.end(), Q[i]) - quest.begin();
		update(0, quest.size() - 1, 1);
	}
	for (long long i = 0; i < M; i++) {
		if (addon[i][0] == 1) {
			X = lower_bound(quest.begin(), quest.end(), addon[i][1]) - quest.begin();
			update(0, quest.size() - 1, 1);
		}
		else {
			//cout << addon[i][2] << addon[i][1] << endl;
			//cout << lower_bound(quest.begin(), quest.end(), addon[i][1]) - quest.begin() << ' ' << upper_bound(quest.begin(), quest.end(), addon[i][2]) - quest.begin() - 1 << endl;
			L = lower_bound(quest.begin(), quest.end(), addon[i][1]) - quest.begin();
			R = upper_bound(quest.begin(), quest.end(), addon[i][2]) - quest.begin() - 1;
			cout << addon[i][2] - addon[i][1] + 1 - getsum(0, quest.size() - 1, 1) << '\n';
		}
	}
}
