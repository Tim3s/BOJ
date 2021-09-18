import sys

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
ans = []
newidx = [0] * len(P)
idx = 0
for i in range(1, len(P)):
    while idx > 0 and P[i] != P[idx]:
        idx = newidx[idx - 1]
    if P[idx] == P[i]:
        idx += 1
        newidx[i] = idx
idx = 0
for i in range(len(T)):
    while idx > 0 and P[idx] != T[i]:
        idx = newidx[idx - 1]
    if P[idx] == T[i]:
        idx += 1
        if idx == len(P):
            ans.append(i - idx + 2)
            idx = newidx[-1]
print(len(ans))
print(*ans)
