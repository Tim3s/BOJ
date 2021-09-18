#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <cstring>
using namespace std;

vector<int> V[1000000], newv[1000000];
int vnum, newvnum, dfn[1000000], low[1000000], used[1000000];
stack<pair<int, int>> S, cuts;


void dfs(int p, int mp = -1) {
	dfn[p] = ++vnum;
	low[p] = vnum;
	for (int q : V[p]) {
		if (q == mp)
			continue;
		if (!dfn[q]) {
			S.push(make_pair(p, q));
			dfs(q, p);
			low[p] = min(low[p], low[q]);
			if (dfn[p] <= low[q]) {
				if (dfn[p] < low[q])
					cuts.push(make_pair(p, q));
				vector<int> tmp;
				while (S.top() != make_pair(p, q)) {
					tmp.push_back(S.top().second);
					S.pop();
				}
				tmp.push_back(S.top().second);
				S.pop();
				int unused = newvnum;
				for (int node : tmp) {
					if (used[node] >= 0) {
						unused = used[node];
						break;
					}
				}
				for (int node: tmp){
					used[node] = unused;
				}
				if (unused == newvnum)
					newvnum++;
			}
		}
		else if (dfn[p] > dfn[q]) {
			low[p] = min(low[p], dfn[q]);
			S.push(make_pair(p, q));
		}
	}
}


pair<int, int> finaldfs(int node, int parent = -1) {
	pair<int, int> res = { -1, node };
	for (int newnode : newv[node]) {
		if (newnode == parent)
			continue;
		res = max(res, finaldfs(newnode, node));
	}
	res.first++;
	return res;
}


int main() {
	int n, m;
	cin >> n >> m;
	int u, v;
	for (int i = 0; i < m; i++) {
		cin >> u >> v;
		V[u].push_back(v);
		V[v].push_back(u);
	}
	memset(used, -1, sizeof(used));
	int ans = -1;
	for (int i = 0; i < n; i++) {
		if (used[i] == -1) {
			while (!S.empty())
				S.pop();
			ans++;
			newvnum = 0;
			dfs(i);
			if (newvnum) {
				if (used[i] == -1) {
					used[i] = newvnum;
					newvnum++;
				}
				while (!cuts.empty()) {
					u = used[cuts.top().first];
					v = used[cuts.top().second];
					newv[u].push_back(v);
					newv[v].push_back(u);
					cuts.pop();
				}
				ans += finaldfs(finaldfs(0).second).first;
				for (int k = 0; k < newvnum; k++) {
					newv[k].clear();
				}
			}
		}
	}
	cout << ans;
}
