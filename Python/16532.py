import sys


def update(x):
    while x <= 100001:
        tree[x] += 1
        x += x & -x


def getsum(x):
    res = 0
    while x:
        res += tree[x]
        x -= x & -x
    return res


Q = int(sys.stdin.readline())
prime = [i for i in range(100001)]
num = [[] for _ in range(100001)]
for i in range(2, 100001):
    num[prime[i]].append(i)
    if prime[i] == i:
        for j in range(i * 2, 100001, i):
            prime[j] = i
tree = [0] * 100001
query = []
for i in range(Q):
    query.append([i] + list(map(int, sys.stdin.readline().split())))
query.sort(key=lambda x: x[2])
idx = 2
for i in range(Q):
    seq, N, K = query[i]
    while idx <= K:
        for v in num[idx]:
            update(v)
        idx += 1
    query[i].append(getsum(N))
query.sort()
for i in range(Q):
    print(query[i][3])
