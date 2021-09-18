#include <iostream>
#include <cmath>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;


pair<int, int> b[101], w[101];
int n, m;
vector<int> bHull, wHull;


int ccw(pair<int, int> p1, pair<int, int> p2) {
	int res = p1.first * p2.second - p1.second * p2.first;
	return res > 0 ? 1 : (res < 0 ? -1 : 0);
}

int cross(pair<int, int> p1, pair<int, int> p2, pair<int, int> p3) {
	return ccw(make_pair(p2.first - p1.first, p2.second - p1.second), make_pair(p3.first - p2.first, p3.second - p2.second));
}

bool intersect(pair<int, int> p1, pair<int, int> p2, pair<int, int> p3, pair<int, int> p4) {
	//cout << p1.first << ' ' << p1.second << endl;
	//cout << p2.first << ' ' << p2.second << endl;
	//cout << p3.first << ' ' << p3.second << endl;
	//cout << p4.first << ' ' << p4.second << endl;
	int x = cross(p1, p2, p3) * cross(p1, p2, p4);
	int y = cross(p3, p4, p1) * cross(p3, p4, p2);
	if (x == 0 && y == 0) {
		//cout << min(p3, p4).first << ' ' << min(p3, p4).second << endl;
		//cout << p2.first << ' ' << p2.second << endl;
		//cout << max(p3, p4).first << ' ' << max(p3, p4).second << endl;
		return min(p1, p2) <= max(p3, p4) && min(p3, p4) <= max(p1, p2);
	}
	return x <= 0 && y <= 0;
}

int dist(pair<int, int> p1, pair<int, int> p2) {
	return (p2.first - p1.first) * (p2.first - p1.first) + (p2.second - p1.second) * (p2.second - p1.second);
}

bool cmpb(pair<int, int> p1, pair<int, int> p2) {
	int res = cross(b[0], p1, p2);
	if (res == 0)
		return dist(b[0], p1) < dist(b[0], p2);
	return res > 0;
}

bool cmpw(pair<int, int> p1, pair<int, int> p2) {
	int res = cross(w[0], p1, p2);
	if (res == 0)
		return dist(w[0], p1) < dist(w[0], p2);
	return res > 0;
}


int main() {
	int T;
	cin >> T;
	while (T--) {
		cin >> n >> m;
		int bidx = 0;
		int widx = 0;
		for (int i = 0; i < n; i++) {
			cin >> b[i].first >> b[i].second;
			if (b[i].second < b[bidx].second || (b[i].second == b[bidx].second && b[i].first < b[bidx].first))
				bidx = i;
		}
		for (int i = 0; i < m; i++) {
			cin >> w[i].first >> w[i].second;
			if (w[i].second < w[widx].second || (w[i].second == w[widx].second && w[i].first < w[widx].first))
				widx = i;
		}
		swap(b[0], b[bidx]);
		swap(w[0], w[widx]);
		sort(b + 1, b + n, cmpb);
		sort(w + 1, w + m, cmpw);
		bHull.clear();
		wHull.clear();
		bHull.push_back(0);
		if (n > 1)
			bHull.push_back(1);
		int idx = 2;
		while (idx < n) {
			while (bHull.size() >= 2) {
				int sec = bHull.back();
				bHull.pop_back();
				int fir = bHull.back();
				if (cross(b[fir], b[sec], b[idx]) > 0) {
					bHull.push_back(sec);
					break;
				}
			}
			bHull.push_back(idx++);
		}
		sort(bHull.begin(), bHull.end());
		bHull.push_back(bHull[0]);
		wHull.push_back(0);
		if (m > 1)
			wHull.push_back(1);
		idx = 2;
		while (idx < m) {
			while (wHull.size() >= 2) {
				int sec = wHull.back();
				wHull.pop_back();
				int fir = wHull.back();
				if (cross(w[fir], w[sec], w[idx]) > 0) {
					wHull.push_back(sec);
					break;
				}
			}
			wHull.push_back(idx++);
		}
		sort(wHull.begin(), wHull.end());
		wHull.push_back(wHull[0]);
		bool invalid = false;
		for (int i = 0; i < bHull.size() - 1; i++) {
			for (int j = 0; j < wHull.size() - 1; j++) {
				if (intersect(b[bHull[i]], b[bHull[i + 1]], w[wHull[j]], w[wHull[j + 1]])) {
					invalid = true;
				}
			}
			if (invalid)
				break;
		}
		if (invalid) {
			cout << "NO\n";
			continue;
		}
		invalid = true;
		for (int i = 0; i < bHull.size() - 1; i++) {
			for (int j = 0; j < wHull.size() - 1; j++) {
				if (cross(b[bHull[i]], b[bHull[i + 1]], w[wHull[j]]) <= 0) {
					invalid = false;
					break;
				}
			}
			if (!invalid)
				break;
		}
		if (invalid) {
			cout << "NO\n";
			continue;
		}
		invalid = true;
		for (int i = 0; i < wHull.size() - 1; i++) {
			for (int j = 0; j < bHull.size() - 1; j++) {
				if (cross(w[wHull[i]], w[wHull[i + 1]], b[bHull[j]]) <= 0) {
					invalid = false;
					break;
				}
			}
			if (!invalid)
				break;
		}
		if (invalid) {
			cout << "NO\n";
			continue;
		}
		cout << "YES\n";
	}
}
