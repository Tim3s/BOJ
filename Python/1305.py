import sys

L = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
newidx = [0] * L
idx = 0
for i in range(1, L):
    while idx > 0 and S[i] != S[idx]:
        idx = newidx[idx - 1]
    if S[idx] == S[i]:
        idx += 1
        newidx[i] = idx
print(L - newidx[-1])
