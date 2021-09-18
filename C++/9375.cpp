#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int n;
		cin >> n;
		string tmp;
		map<string, int> mymap;
		for (int j = 0; j < n; j++) {
			cin >> tmp >> tmp;
			if (mymap.find(tmp) == mymap.end())
				mymap[tmp] = 1;
			else
				mymap[tmp]++;
		}
		int res = 1;
		for (auto iter = mymap.begin(); iter != mymap.end(); iter++) {
			res *= iter->second + 1;
		}
		res--;
		cout << res << '\n';
	}
}
