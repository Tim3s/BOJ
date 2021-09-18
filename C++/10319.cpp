#include <vector>
#include <iostream>
#include <cstring>
//#include <cassert>
#include <algorithm>
#include <cmath>
#include <queue>
#include <climits>
using namespace std;

struct edge {
	int x, c, f;
	edge* d;
} nedge[422402];

vector<edge*> network[101002];
edge* pre[101002];
int num_edge;


void make_edge(int p, int q, int cap) {
	nedge[num_edge] = { q, cap, 0, 0 };
	edge* now1 = &nedge[num_edge++];
	nedge[num_edge] = { p, 0, 0, 0 };
	edge* now2 = &nedge[num_edge++];
	now1->d = now2;
	now2->d = now1;
	//assert(p < 101002);
	network[p].push_back(now1);
	network[q].push_back(now2);
}


int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	while (T--) {
		num_edge = 0;
		int N;
		cin >> N;
		int i, g, t;
		cin >> i >> g >> t;
		i -= 1;
		int length = N * (t + 1) + 2;
		for (int seq = 0; seq < length; seq++) {
			network[seq].clear();
		}
		int s = length - 2;
		int e = length - 1;
		for (int start = i; start < s; start += N) {
			make_edge(s, start, g);
		}
		for (int i = 0; i < t * N; i += N) {
			for (int j = i; j < i + N; j++) {
				make_edge(j, j + N, g);
			}
		}
		int M;
		cin >> M;
		int x;
		while (M--) {
			cin >> x;
			x--;
			for (int i = x; i < s; i += N) {
				make_edge(i, e, g);
			}
		}
		int r;
		cin >> r;
		int a, b, p, k;
		while (r--) {
			cin >> a >> b >> p >> k;
			a--;
			b--;
			for (int i = 0; i < s; i += N) {
				if (i + N * k < s) {
					make_edge(i + a, i + N * k + b, p);
					continue;
				}
				break;
			}
		}
		int tmp = 0;
		while (true) {
			queue<int> Q;
			Q.push(s);
			memset(pre, 0, sizeof(pre));
			//for (int i = 0; i < length; i++) {
			//	pre[i] = NULL;
			//}
			//assert(pre[e] == NULL);
			while (!Q.empty()) {
				int p = Q.front();
				Q.pop();
				for (edge* q : network[p]) {
					//assert(q != NULL);
					if (pre[q->x] == NULL && q->c > q->f) {
						pre[q->x] = q;
						//assert(pre[q->x] != NULL);
						Q.push(q->x);
					}
				}
			}
			if (pre[e] == 0)
				break;
			int val = INT_MAX;
			for (int i = e; i != s; i = pre[i]->d->x) {
				//assert(!(i != e && i != s && pre[i] == NULL));
				val = min(val, pre[i]->c - pre[i]->f);
			}
			for (int i = e; i != s; i = pre[i]->d->x) {
				pre[i]->f += val;
				pre[i]->d->f -= val;
			}
			tmp += val;
			if (tmp > g)
				break;
		}
		cout << min(tmp, g) << '\n';
	}
}
