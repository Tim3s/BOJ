#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
using namespace std;

stack<int> s;
bool visited1[500111];
int visited2[500111], idx(1), tmp[50000];
vector<int> front[500111], pre[500111];

int inverse(int a) {
	return 500011 - a;
}

void dfs1(int n) {
	visited1[n] = true;
	for (auto v : front[n]) {
		if (!visited1[v])
			dfs1(v);
	}
	s.push(n);
}

void dfs2(int n) {
	visited2[n] = idx;
	for (auto v : pre[n]) {
		if (!visited2[v])
			dfs2(v);
	}
}

void make(int a, int b) {
	front[a].push_back(b);
	pre[b].push_back(a);
}

int main() {
	int N, M;
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> tmp[i];
	cin >> M;
	for (int i = 0; i < N; i++) {
		if (tmp[i]) {
			int cur = i * 5;
			for (int j = 0; j < 5; j++) {
				cur++;
				if (tmp[i] & 1 << j) {
					make(inverse(cur), cur);
					continue;
				}
				make(cur, inverse(cur));
			}
		}
	}
	for (int i = 0; i < 5 * N; i += 5) {
		int tmp3 = i + 3;
		int tmp4 = i + 4;
		int tmp5 = i + 5;
		make(inverse(tmp5), tmp4);
		make(tmp5, inverse(tmp4));
		make(tmp5, inverse(tmp3));
		make(inverse(tmp4), tmp5);
		make(tmp4, inverse(tmp5));
		make(tmp3, inverse(tmp5));
	}
	for (int nothing = 0; nothing < M; nothing++) {
		char t;
		int x, y, z;
		cin >> t >> x >> y >> z;
		x = (x * 5) - 5;
		y = (y * 5) - 5;
		if (t == '&') {
			for (int j = 0; j < 5; j++) {
				x++;
				y++;
				if (z & 1 << j) {
					make(inverse(x), x);
					make(inverse(y), y);
					continue;
				}
				make(x, inverse(y));
				make(y, inverse(x));
			}
			continue;
		}
		for (int j = 0; j < 5; j++) {
			x++;
			y++;
			if (z & 1 << j) {
				make(inverse(x), y);
				make(inverse(y), x);
				continue;
			}
			make(x, inverse(x));
			make(y, inverse(y));
		}
	}

	for (int i = inverse(5 * N); i < inverse(0); i++) {
		if (!visited1[i])
			dfs1(i);
	}
	for (int i = 1; i <= 5 * N; i++) {
		if (!visited1[i])
			dfs1(i);
	}

	while (!s.empty()) {
		int cur = s.top();
		s.pop();
		if (!visited2[cur]) {
			dfs2(cur);
			idx++;
		}
	}
	int* ans = new int[5 * N + 1];
	for (int i = 1; i <= 5 * N; i++) {
		if (visited2[i] == visited2[inverse(i)]) {
			cout << 0;
			return 0;
		}
		if (visited2[i] > visited2[inverse(i)]) {
			ans[i] = 1;
		}
		else
			ans[i] = 0;
	}
	cout << 1 << '\n';
	for (int i = 1; i < 5 * N; i += 5) {
		int res = 0;
		for (int j = 0; j < 5; j++)
			res += (1 << j) * ans[i + j];
		cout << res << ' ';
	}
}
