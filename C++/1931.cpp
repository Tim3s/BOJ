#include <iostream>
#include <algorithm>
using namespace std;

bool endtime(pair<int, int> f, pair <int, int> s);

int main() {
	int N, S, E;
	cin >> N;
	pair<int, int>* time = new pair<int, int>[N];
	for (int i = 0; i < N; i++)
		cin >> time[i].first >> time[i].second;
	sort(time, time + N, endtime);
	int cur = time[0].second;
	int cnt = 1;
	for (int i = 1; i < N; i++) {
		if (time[i].first >= cur) {
			cur = time[i].second;
			cnt++;
		}
	}
	cout << cnt;
}

bool endtime(pair<int, int> f, pair<int, int> s)
{
	if (f.second == s.second)
		return f.first < s.first;
	return f.second < s.second;
}
