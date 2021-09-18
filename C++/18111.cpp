#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N, M, B, tmp, totalheight(0);
	int* height = new int[257];
	cin >> N >> M >> B;
	for (int i = 0; i < 257; i++)
		height[i] = 0;
	for(int i = 0; i < N * M; i++){
		cin >> tmp;
		height[tmp]++;
		totalheight += tmp;
	}
	int cur = min((totalheight + B) / (N * M), 256);
	int time(0);
	int below(0), above(0);
	for (int i = 0; i < cur; i++) {
		time += (cur - i) * height[i];
		below += height[i];
	}
	for (int i = cur + 1; i < 257; i++) {
		time += (i - cur) * height[i] * 2;
		above += height[i];
	}
	while (true) {
		if (cur == 0)
			break;
		above += height[cur];
		if (above * 2 - below < 0) {
			cur--;
			time += above * 2 - below;
		}
		else
			break;
		below -= height[cur];
	}
	cout << time << " " << cur;
}
