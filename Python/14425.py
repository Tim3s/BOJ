import sys

base = set()
N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    base.add(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(M):
    if sys.stdin.readline().rstrip() in base:
        cnt += 1
print(cnt)
