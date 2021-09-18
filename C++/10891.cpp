#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int dfn[100001], vnum(0);
vector<int> V[100001];

int dfs(int p, int mp = -1) {
	dfn[p] = ++vnum;
	int res = 0;
	for (int q : V[p]) {
		if (q == mp)
			continue;
		if (!dfn[q]) {
			int tmp = dfs(q, p);
			if (res && tmp) {
				cout << "Not cactus";
				exit(0);
			}
			else if (tmp)
				res = tmp;
		}
		else if (dfn[p] > dfn[q]){
			if (res) {
				cout << "Not cactus";
				exit(0);
			}
			res = q;
		}
	}
	return ((res == p) ? 0 : res);
}


int main() {
	int N, M;
	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		int x, y;
		cin >> x >> y;
		V[x].push_back(y);
		V[y].push_back(x);
	}
	dfs(1);
	cout << "Cactus";
}
