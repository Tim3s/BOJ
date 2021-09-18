import sys

N, M = map(int, sys.stdin.readline().split())
profit = [[0] for _ in range(N + 1)]
profit[0] = [0] * M
for i in range(N):
    money = list(map(int, sys.stdin.readline().split()))
    profit[money[0]] = money[1:]
ans = [[0] * (N + 1) for _ in range(M)]
idx = [[0] * (N + 1) for _ in range(M)]
ans[0] = [profit[i][0] for i in range(N + 1)]
for i in range(1, M):
    for j in range(1, N + 1):
        tmp = [ans[i - 1][k] + profit[j - k][i] for k in range(j + 1)]
        ans[i][j] = max(tmp)
        idx[i][j] = tmp.index(ans[i][j])
print(ans[-1][-1])
company = M - 1
money = N
ans = []
while company > 0:
    ans.append(money - idx[company][money])
    money = idx[company][money]
    company -= 1
ans.append(money)
print(' '.join(list(map(str, reversed(ans)))))
