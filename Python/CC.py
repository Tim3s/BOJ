import sys

for _ in range(int(sys.stdin.readline())):
    sys.stdin.readline()
    k, n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    ap = 0
    bp = 0
    res = ''
    possible = True
    while ap < n or bp < m:
        if ap < n and not a[ap]:
            res += ' 0'
            ap += 1
            k += 1
        elif bp < m and not b[bp]:
            res += ' 0'
            bp += 1
            k += 1
        elif ap < n and a[ap] <= k:
            res += ' ' + str(a[ap])
            ap += 1
        elif bp < m and b[bp] <= k:
            res += ' ' + str(b[bp])
            bp += 1
        else:
            possible = False
            break
    if possible:
        print(res[1:])
    else:
        print(-1)
