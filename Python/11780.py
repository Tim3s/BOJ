import sys
import copy

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
route = [[0] * (n + 1) for _ in range(n + 1)]
bus = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if not 0 < bus[a][b] <= c:
        bus[a][b] = c
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j != k and bus[i][k] and bus[k][j] and not 0 < bus[i][j] <= bus[i][k] + bus[k][j]:
                bus[i][j] = bus[i][k] + bus[k][j]
                route[i][j] = k
for i in range(1, n + 1):
    print(' '.join(map(str, bus[i][1:])))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if not bus[i][j]:
            print(0)
            continue
        ans = [i]
        if route[i][j]:
            ans.append(route[i][j])
        ans.append(j)
        cur = [i, j]
        while cur != ans:
            cur = copy.deepcopy(ans)
            ans = [cur[0]]
            for k in range(1, len(cur)):
                if route[cur[k-1]][cur[k]]:
                    ans.append(route[cur[k-1]][cur[k]])
                ans.append(cur[k])
        print(len(ans), ' '.join(map(str, ans)))
