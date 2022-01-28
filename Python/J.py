import sys

N = int(sys.stdin.readline())
a = list(map(lambda x: ord(x) - 97, sys.stdin.readline().split()))
K = ord(sys.stdin.readline().rstrip()) - 97
S = list(map(lambda x: ord(x) - 97, list(sys.stdin.readline().rstrip())))
if K not in S:
    print('NO')
    sys.exit(0)
init = S.index(K)
if init != 0:
    cur = [S[:init]]
    last = K
    d = []
    while last == cur[-1]:
        cur.pop()
        d.append()
    while cur:
        if not d:
            while last == cur[-1]:
                cur.pop()

        if cur[-1] != d[-1]:
            d.append(a[d[-1]])
            if len(d) > len(cur):
                print('NO')
                sys.exit(0)
        else:
            d.pop()
            cur.pop()
if init != N - 1:
    cur = [S[i] for i in range(N - 1, init, -1)]
    d = [a[K]]
    while cur:
        if cur[-1] != d[-1]:
            d.append(a[d[-1]])
            if len(d) > len(cur):
                print('NO')
                sys.exit(0)
        else:
            d.pop()
            cur.pop()
print('YES')
