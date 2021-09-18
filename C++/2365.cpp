#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <climits>
using namespace std;

int N, row[50], column[50], length, last, base[2602][2602], flow[2602][2602], l, r, mid, ans, tmpsum, val, cur, pre[2602];
vector<int> network[2602];

void init(int x) {
	memcpy(flow, base, sizeof(base));
	cur = N;
	for (int i = 1; i <= N; i++) {
		for (int j = last - N; j < last; j++) {
			cur++;
			flow[i][cur] = x;
		}
	}
}


int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> row[i];
		tmpsum += row[i];
		r = max(r, row[i]);
	}
	for (int i = 0; i < N; i++) {
		cin >> column[i];
		r = max(r, column[i]);
	}
	length = N * N + 2 * N + 2;
	last = length - 1;
	for (int i = 1; i <= N; i++) {
		network[0].push_back(i);
		network[i].push_back(0);
		base[0][i] = row[i - 1];
		network[last].push_back(last - i);
		network[last - i].push_back(last);
		base[last - i][last] = column[N - i];
	}
	cur = N;
	for (int i = 1; i <= N; i++) {
		for (int j = last - N; j < last; j++) {
			cur++;
			network[i].push_back(cur);
			network[cur].push_back(i);
			network[cur].push_back(j);
			network[j].push_back(cur);
			base[cur][j] = column[N + j - last];
		}
	}
	ans = r;
	while (r >= l) {
		mid = (l + r) / 2;
		init(mid);
		int tmp = 0;
		while (true) {
			queue<int> q;
			q.push(0);
			memset(pre, -1, sizeof(pre));
			while (!q.empty()) {
				int u = q.front();
				q.pop();
				for (int v : network[u]) {
					if (pre[v] == -1 && flow[u][v]) {
						pre[v] = u;
						q.push(v);
					}
				}
			}
			if (pre[last] == -1)
				break;
			cur = last;
			val = INT_MAX;
			while (cur) {
				val = min(val, flow[pre[cur]][cur]);
				cur = pre[cur];
			}
			cur = last;
			while (cur) {
				flow[pre[cur]][cur] -= val;
				flow[cur][pre[cur]] += val;
				cur = pre[cur];
			}
			tmp += val;
		}
		if (tmp == tmpsum) {
			r = mid - 1;
			ans = mid;
		}
		else
			l = mid + 1;
	}
	cout << ans << '\n';
	init(ans);
	while (true) {
		queue<int> q;
		q.push(0);
		memset(pre, -1, sizeof(pre));
		while (!q.empty()) {
			int u = q.front();
			q.pop();
			for (int v : network[u]) {
				if (pre[v] == -1 && flow[u][v]) {
					pre[v] = u;
					q.push(v);
				}
			}
		}
		if (pre[last] == -1)
			break;
		cur = last;
		val = INT_MAX;
		while (cur) {
			val = min(val, flow[pre[cur]][cur]);
			cur = pre[cur];
		}
		cur = last;
		while (cur) {
			flow[pre[cur]][cur] -= val;
			flow[cur][pre[cur]] += val;
			cur = pre[cur];
		}
	}
	for (int i = N + 1; i <= N * N + N; i += N) {
		int tmp = (i - 1) / N;
		for (int j = i; j < i + N; j++) {
			cout << flow[j][tmp] << ' ';
		}
		cout << '\n';
	}
}
