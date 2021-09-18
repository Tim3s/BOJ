#include <iostream>
using namespace std;

class Queue {
private:
	int size;
	pair<int, int>* queue;
	int f, l;
	bool empty;
public:
	Queue(int n);
	pair<int, int> dequeue();
	void enqueue(int a, int b);
	void enqueue(pair<int, int> a);
	bool find();
};

int main() {
	cin.tie(NULL);
	int loop, N, M, cur;
	cin >> loop;
	for (int i = 0; i < loop; i++) {
		cin >> N >> M;
		int* doc = new int[N];
		Queue queue = Queue(N);
		for (int j = 0; j < N; j++) {
			cin >> cur;
			queue.enqueue(j, cur);
		}
		if (N == 1)
			cout << 1 << "\n";
		else {
			int cnt = 1;
			while (true) {
				if (queue.find())
					queue.enqueue(queue.dequeue());
				else {
					if (queue.dequeue().first == M)
						break;
					else
						cnt++;
				}
			}
			cout << cnt << "\n";
		}
	}
}

Queue::Queue(int n)
{
	size = n;
	queue = new pair<int, int>[n];
	empty = true;
}

pair<int, int> Queue::dequeue()
{
	int tmp = f;
	f = (f + 1) % size;
	return queue[tmp];
}

void Queue::enqueue(int a, int b)
{
	if (empty) {
		queue[0].first = a;
		queue[0].second = b;
		f = 0;
		l = 0;
		empty = false;
	}
	else {
		l = (l + 1) % size;
		queue[l].first = a;
		queue[l].second = b;
	}
}

void Queue::enqueue(pair<int, int> a)
{
	l = (l + 1) % size;
	queue[l] = a;
}

bool Queue::find()
{
	for (int i = (f + 1) % size; i != (l + 1) % size; i = (i + 1) % size) {
		if (queue[i].second > queue[f].second)
			return true;
	}
	return false;
}
