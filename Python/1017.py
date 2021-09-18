import sys


def dfs(p):
    vis[p] = True
    for q in V[p]:
        if b[q] == -1 or (not vis[b[q]] and dfs(b[q])):
            a[p] = q
            b[q] = p
            return True
    return False


prime = [True] * 2000
for i in range(4, 2000, 2):
    prime[i] = False
for i in range(3, 2000, 2):
    if prime[i]:
        for j in range(i * i, 2000, 2 * i):
            prime[j] = False
sys.stdin.readline()
num = list(map(int, sys.stdin.readline().split()))
odd = [i for i in num if i % 2]
even = [i for i in num if not i % 2]
if even[0] == num[0]:
    odd, even = even, odd
N = len(odd)
M = len(even)
if N != M:
    print(-1)
    sys.exit(0)
ans = []
V = [set() for _ in range(N)]
for i in range(N):
    for j in range(M):
        if prime[odd[i] + even[j]]:
            V[i].add(j)
first = V[0]
V[0] = set()
for node in first:
    tmp = 0
    revise = set()
    for i in range(1, N):
        if node in V[i]:
            V[i].remove(node)
            revise.add(i)
    V[0] = {node}
    a = [-1] * N
    b = [-1] * M
    a[0] = node
    b[node] = 0
    for i in range(1, N):
        vis = [False] * N
        if dfs(i):
            tmp += 1
    for i in revise:
        V[i].add(node)
    if tmp == M - 1:
        ans.append(even[node])
if not ans:
    print(-1)
    sys.exit(0)
ans.sort()
print(*ans)
