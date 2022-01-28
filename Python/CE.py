import sys

for _ in range(int(sys.stdin.readline())):
    sys.stdin.readline()
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    t = list(map(int, sys.stdin.readline().split()))
    inc = sorted([(t[i], i) for i in range(k)])
    res = [2 * 10 ** 9] * n
    for i in range(k):
        res[a[i]] = t[i]
    for i in inc:
        idx = i[1]
        tmp = i[0] + 1
        loc = a[idx]
        for j in range(1, max(loc + 1, n - loc)):
            done = False
            if j < n - loc and res[loc + j] > tmp:
                res[loc + j] = tmp
                done = True
            if j <= loc and res[loc - j] > tmp:
                res[loc - j] = tmp
                done = True
            tmp += 1
            if not done:
                break
    print(*res)
