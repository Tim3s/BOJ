#include <iostream>
using namespace std;

class Queue {
private:
	int size;
	int* queue;
	int f, l;
	bool empty;
public:
	Queue(int n);
	int dequeue();
	void enqueue(int a);
};

int main() {
	cin.tie(NULL);
	int N;
	cin >> N;
	Queue queue = Queue(N);
	for (int i = 1; i <= N; i++)
		queue.enqueue(i);
	for (int i = 1; i < N; i++) {
		queue.dequeue();
		queue.enqueue(queue.dequeue());
	}
	cout << queue.dequeue();

}

Queue::Queue(int n)
{
	size = n;
	queue = new int[n];
	empty = true;
}

int Queue::dequeue()
{
	int tmp = f;
	f = (f + 1) % size;
	return queue[tmp];
}

void Queue::enqueue(int a)
{
	if (empty) {
		queue[0] = a;
		f = 0;
		l = 0;
		empty = false;
	}
	else {
		l = (l + 1) % size;
		queue[l] = a;
	}
}
