import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
all = [0] * 1000001
for a in A:
    all[a] += 1
for b in B:
    if all[b]:
        all[b] -= 1
print(sum(all))
