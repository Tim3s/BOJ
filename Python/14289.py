import sys


def mul(a, b):
    return [[sum([a[i][k] * b[k][j] for k in range(n)]) % 1000000007 for j in range(n)] for i in range(n)]


n, m = map(int, sys.stdin.readline().split())
univ = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    univ[a][b] = univ[b][a] = 1
D = int(sys.stdin.readline())
ans = [[0] * n for _ in range(n)]
for i in range(n):
    ans[i][i] = 1
while D > 0:
    if D % 2:
        ans = mul(ans, univ)
    univ = mul(univ, univ)
    D //= 2
print(ans[0][0])
