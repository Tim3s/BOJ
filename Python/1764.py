import sys

N, M = list(map(int, sys.stdin.readline().split()))
listen = set()
final = []
for i in range(N):
    listen.add(sys.stdin.readline().rstrip())
for i in range(M):
    tmp = sys.stdin.readline().rstrip()
    if tmp in listen:
        final.append(tmp)
print(len(final))
print("\n".join(sorted(final)))
