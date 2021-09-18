#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long

int cnt = 0;
int into[200001];
int out[200001];
int inverse[200001];
int color[200001];
int i, j, c, v, N, M, C, a, b;
vector<int> E[200001], tree[524288];


void dfs(int x);
void init(int left, int right, int idx);
ll getsum(int left, int right, int idx);


int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> N >> M >> C;
	for (int i = 1; i <= N; i++) {
		cin >> color[i];
	}
	for (int i = 0; i < N - 1; i++) {
		cin >> a >> b;
		E[a].push_back(b);
		E[b].push_back(a);
	}
	dfs(1);
	init(1, N, 1);
	ll ans = 0;
	for (int k = 0; k < M; k++) {
		cin >> v >> c;
		i = into[v];
		j = out[v];
		ans += getsum(1, N, 1);
		ans %= 1000000007;
	}
	cout << ans;
}


void dfs(int x) {
	into[x] = ++cnt;
	inverse[cnt] = color[x];
	for (unsigned int i = 0; i < E[x].size(); i++) {
		if (into[E[x][i]] == 0) {
			dfs(E[x][i]);
		}
	}
	out[x] = cnt;
}


void init(int left, int right, int idx) {
	if (left == right) {
		tree[idx].push_back(inverse[left]);
	}
	else {
		int tmp = idx << 1;
		int mid = (left + right) >> 1;
		init(left, mid, tmp);
		init(mid + 1, right, tmp + 1);
		for (auto v : tree[tmp]) {
			tree[idx].push_back(v);
		}
		for (auto v : tree[tmp + 1]) {
			tree[idx].push_back(v);
		}
		sort(tree[idx].begin(), tree[idx].end());
	}
}


ll getsum(int left, int right, int idx) {
	if (j < left || i > right) {
		return 0;
	}
	if (i <= left && right <= j) {
		return upper_bound(tree[idx].begin(), tree[idx].end(), c) - tree[idx].begin();
	}
	int mid = (left + right) >> 1;
	idx <<= 1;
	return getsum(left, mid, idx) + getsum(mid + 1, right, idx + 1);
}
