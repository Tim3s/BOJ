import sys


def dfs(starti, endi, startp, endp):
    stack = [(starti, endi, startp, endp)]
    while stack:
        starti, endi, startp, endp = stack.pop()
        if starti >= endi:
            continue
        root = postfix[endp - 1]
        print(root, end=' ')
        infixroot = infix.index(root)
        stack.append((infixroot + 1, endi, startp + infixroot - starti, endp - 1))
        stack.append((starti, infixroot, startp, startp + infixroot - starti))


n = int(sys.stdin.readline())
infix = list(map(int, sys.stdin.readline().split()))
postfix = list(map(int, sys.stdin.readline().split()))
dfs(0, n, 0, n)
