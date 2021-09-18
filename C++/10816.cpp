#include <iostream>
#include <map>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	map<int, int> mymap;
	int N;
	cin >> N;
	int cnum;
	for (int i = 0; i < N; i++) {
		cin >> cnum;
		if (mymap.find(cnum) == mymap.end())
			mymap[cnum] = 1;
		else
			mymap[cnum]++;
	}
	int M;
	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> cnum;
		if (mymap.find(cnum) == mymap.end())
			cout << "0 ";
		else
			cout << mymap[cnum] << " ";
	}
}
