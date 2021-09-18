import sys
sys.setrecursionlimit(10 ** 9)


def dfs(x):
    res = memo[x]
    if res != -1:
        return res
    res = 0
    for v, w in cave[x]:
        tmp = dfs(v) - w
        if tmp > res:
            res = tmp
            nextcave[x] = v
    res += V[x]
    memo[x] = res
    return res


T = int(sys.stdin.readline())
for _ in range(T):
    N, E = map(int, sys.stdin.readline().split())
    V = [0] + list(map(int, sys.stdin.readline().split()))
    cave = [[] for _ in range(N + 1)]
    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().split())
        cave[a].append([b, c])
    memo = [-1] * (N + 1)
    nextcave = [-1] * (N + 1)
    print(dfs(1), end=' ')
    cur = 1
    ans = []
    while cur != -1:
        ans.append(str(cur))
        cur = nextcave[cur]
    print(len(ans))
    print(' '.join(ans))
