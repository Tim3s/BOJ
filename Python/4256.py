import sys


def bfs(starti, endi, startp, endp):
    res = []
    stack = [(starti, endi, startp, endp)]
    while stack:
        starti, endi, startp, endp = stack.pop()
        if starti >= endi:
            continue
        root = prefix[startp]
        res.append(root)
        infixroot = infix.index(root)
        stack.append((starti, infixroot, startp + 1, startp + infixroot - starti + 1))
        stack.append((infixroot + 1, endi, endp - endi + infixroot + 1, endp))
    return res


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    prefix = list(map(int, sys.stdin.readline().split()))
    infix = list(map(int, sys.stdin.readline().split()))
    print(' '.join(map(str, reversed(bfs(0, n, 0, n)))))
