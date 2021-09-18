#include <iostream>
#include <vector>
#include <cstring>
#include <stack>
using namespace std;

vector<int> V[100001], ans;
bool used[100001], finished, ac[100001];
int dfn[100001], low[100001], vnum;
stack<int> S, NS;


void dfs(int p, int mp = -1) {
	dfn[p] = ++vnum;
	low[p] = vnum;
	S.push(p);
	int child = 0;
	for (int q : V[p]) {
		if (q == mp || used[q])
			continue;
		if (!dfn[q]) {
			child++;
			dfs(q, p);
			low[p] = min(low[p], low[q]);
			if (dfn[p] <= low[q]) {
				if (mp != -1 || child >= 2)
					ac[p] = true;
				while (!NS.empty()) {
					NS.pop();
				}
				int cuts = 0;
				while (S.top() != p) {
					if (ac[S.top()]) {
						cuts++;
					}
				}
			}
		}
	}
}




int main() {
	int N, M;
	cin >> N >> M;
	int u, v;
	for (int i = 0; i < M; i++) {
		cin >> u >> v;
		V[u].push_back(v);
		V[v].push_back(u);
	}
	while (!finished) {

		for (int i = 1; i <= N; i++) {
			dfs(i);
		}
	}
}
