#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;

vector<int> V[100111], newv[100111], leaf;
int vnum, newvnum, dfn[100111], low[100111], used[100111], reversing[100111];
stack<pair<int, int>> S, cuts;
bool visited[100111];


int dfs(int p, int mp = -1) {
	dfn[p] = ++vnum;
	low[p] = vnum;
	int cnt = 0;
	for (int q : V[p]) {
		if (q == mp) {
			if (!cnt++)
				continue;
		}
		if (!dfn[q]) {
			S.push(make_pair(p, q));
			int multi = dfs(q, p);
			low[p] = min(low[p], low[q]);
			if (dfn[p] <= low[q]) {
				if (dfn[p] < low[q] && multi == 1)
					cuts.push(make_pair(p, q));
				vector<int> tmp;
				while (S.top() != make_pair(p, q)) {
					tmp.push_back(S.top().second);
					S.pop();
				}
				tmp.push_back(S.top().second);
				//if (find(tmp.begin(), tmp.end(), p) == tmp.end())
				//	cuts.push(make_pair(p, q));
				S.pop();
				int unused = newvnum;
				for (int node : tmp) {
					if (used[node] >= 0) {
						unused = used[node];
						break;
					}
				}
				for (int node : tmp) {
					used[node] = unused;
				}
				if (unused == newvnum) {
					reversing[newvnum++] = q;
				}
			}
		}
		else if (dfn[p] > dfn[q]) {
			low[p] = min(low[p], dfn[q]);
			S.push(make_pair(p, q));
		}
	}
	return cnt;
}


void dfs2(int x) {
	visited[x] = true;
	if (newv[x].size() == 1) {
		leaf.push_back(x);
	}
	for (int node : newv[x]) {
		if (!visited[node]) {
			dfs2(node);
		}
	}
}


int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	int N, M;
	cin >> N >> M;
	int C1, C2;
	for (int i = 0; i < M; i++) {
		cin >> C1 >> C2;
		V[C1].push_back(C2);
		V[C2].push_back(C1);
	}
	memset(used, -1, sizeof(used));
	vnum = 1;
	dfs(1);
	if (used[1] == -1) {
		reversing[newvnum] = 1;
		used[1] = newvnum++;
	}
	if (newvnum == 1) {
		cout << 0;
		return 0;
	}
	while (!cuts.empty()) {
		int left = used[cuts.top().first];
		int right = used[cuts.top().second];
		cuts.pop();
		if (left == right)
			continue;
		newv[left].push_back(right);
		newv[right].push_back(left);
	}
	dfs2(0);
	cout << (leaf.size() + 1) / 2 << '\n';
	if (leaf.size() % 2) {
		int left = 0;
		int right = leaf.size() / 2 + 1;
		while (right != leaf.size()) {
			cout << reversing[leaf[left++]] << ' ' << reversing[leaf[right++]] << '\n';
		}
		cout << reversing[leaf[leaf.size() / 2]] << ' ' << reversing[leaf[0]] << '\n';
	}
	else {
		int left = 0;
		int right = leaf.size() / 2;
		while (right != leaf.size()) {
			cout << reversing[leaf[left++]] << ' ' << reversing[leaf[right++]] << '\n';
		}
	}
}
