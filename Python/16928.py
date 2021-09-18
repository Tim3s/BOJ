import sys
from collections import deque


def bfs():
    visited = [False] * 101
    visited[1] = True
    q = deque([(1, 0)])
    while True:
        s, time = q.popleft()
        time += 1
        for i in range(1, 7):
            tmp = game[s + i]
            if tmp == 100:
                return time
            if not visited[tmp]:
                visited[tmp] = True
                q.append((tmp, time))


N, M = map(int, sys.stdin.readline().split())
game = [i for i in range(101)]
for i in range(N + M):
    x, y = map(int, sys.stdin.readline().split())
    game[x] = y
print(bfs())
