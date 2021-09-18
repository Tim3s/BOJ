import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    num = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    done = [False] * n
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        loop = True
        curvisit = set()
        curvisit.add(i)
        while True:
            i = num[i]
            if i in curvisit:
                break
            if visited[i]:
                loop = False
                break
            visited[i] = True
            curvisit.add(i)
        if loop:
            while not done[i]:
                done[i] = True
                i = num[i]
    ans = 0
    for i in range(n):
        if not done[i]:
            ans += 1
    print(ans)
