#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
using namespace std;

char isle[2001][2001];
int visited[2001][2001], done[4000000], dfn[4000001], idx(0), vnum(0), N, M;
bool land[4000000], ac[4000000];
vector<int> V[4000000];
stack<int> S;


int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };


void dfs(int x, int y) {
	visited[x][y] = idx;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (!(0 <= nx && nx < N && 0 <= ny && ny < M))
			continue;
		if (isle[x][y] == isle[nx][ny] && !visited[nx][ny])
			dfs(nx, ny);
		else if (isle[x][y] != isle[nx][ny] && visited[nx][ny]) {
			if (done[visited[nx][ny]] != idx) {
				V[idx].push_back(visited[nx][ny]);
				V[visited[nx][ny]].push_back(idx);
				done[idx] = idx;
				done[visited[nx][ny]] = idx;
			}
		}
	}
}


void get(int p) {
	dfn[p] = ++vnum;
	int ret = idx;
	S.push(p);
	for (int q : V[p]) {
		if (!dfn[q]) {
			get(q);
			if (land[p] and dfn[q] == dfn[p]) {
				while (!S.empty() and S.top() != p) {
					ac[S.top()] = true;
					S.pop();
				}
			}
			S.push(p);
		}
		ret = min(ret, dfn[q]);
	}
	dfn[p] = ret;
}


int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++)
		cin >> isle[i];
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (!visited[i][j]) {
				idx += 1;
				land[idx] = (isle[i][j] == '#');
				dfs(i, j);
			}
		}
	}
	get(1);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (isle[i][j] == '.') {
				cout << '.';
				continue;
			}
			if (ac[visited[i][j]]) {
				cout << 'X';
				continue;
			}
			cout << 'O';
		}
		cout << '\n';
	}
	return 0;
}
