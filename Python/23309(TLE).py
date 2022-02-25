import sys


N, M = map(int, sys.stdin.readline().split())
initial = list(map(int, sys.stdin.readline().split()))
nxt = [-1] * 1000001
prev = [-1] * 1000001
for i in range(-1, N - 1):
    nxt[initial[i]] = initial[i+1]
    prev[initial[i+1]] = initial[i]
for _ in range(M):
    info = sys.stdin.readline().split()
    if info[0] == 'BN':
        i = int(info[1])
        j = int(info[2])
        print(nxt[i])
        prev[nxt[i]] = j
        nxt[j] = nxt[i]
        nxt[i] = j
        prev[j] = i
        continue
    if info[0] == 'BP':
        i = int(info[1])
        j = int(info[2])
        print(prev[i])
        nxt[prev[i]] = j
        prev[j] = prev[i]
        prev[i] = j
        nxt[j] = i
        continue
    if info[0] == 'CN':
        i = int(info[1])
        print(nxt[i])
        nxt[i] = nxt[nxt[i]]
        prev[nxt[i]] = i
        continue
    i = int(info[1])
    print(prev[i])
    prev[i] = prev[prev[i]]
    nxt[prev[i]] = i
