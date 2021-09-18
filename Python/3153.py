import sys
sys.setrecursionlimit(10 ** 9)


def dfs1(n):
    visited[n] = True
    for v in forward[n]:
        if not visited[v]:
            dfs1(v)
    stack.append(n)


def dfs2(n):
    visited[n] = idx
    for v in backward[n]:
        if visited[v] == -1:
            dfs2(v)


def make(a, b):
    forward[a].add(b)
    backward[b].add(a)


R, S = map(int, sys.stdin.readline().split())
tower = []
clone = []
toweridx = dict()
company = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
tidx = 1
for i in range(R):
    for j in range(S):
        if company[i][j] == 'n':
            clone.append((i, j))
        elif company[i][j] == 'T':
            tower.append((i, j))
            toweridx[(i, j)] = tidx
            tidx += 2
length = tidx - 1
forward = [set() for _ in range(2 * length + 1)]
backward = [set() for _ in range(2 * length + 1)]
for i, j in clone:
    right = 0
    for k in range(j - 1, -1, -1):
        if company[i][k] == 'T':
            right = toweridx[(i, k)] + 1
            break
        elif company[i][k] == '#':
            break
    left = 0
    for k in range(j + 1, S):
        if company[i][k] == 'T':
            left = toweridx[(i, k)] + 1
            break
        elif company[i][k] == '#':
            break
    down = 0
    for k in range(i - 1, -1, -1):
        if company[k][j] == 'T':
            down = toweridx[(k, j)]
            break
        elif company[k][j] == '#':
            break
    up = 0
    for k in range(i + 1, R):
        if company[k][j] == 'T':
            up = toweridx[(k, j)]
            break
        elif company[k][j] == '#':
            break
    if (left and right) or (not left and not right):
        if left and right:
            make(-left, left)
            make(right, -right)
        if down:
            make(-down, down)
            continue
        make(up, -up)
        continue
    if (up and down) or (not up and not down):
        if up and down:
            make(-up, up)
            make(down, -down)
        if right:
            make(-right, right)
            continue
        make(left, -left)
        continue
    if down:
        if right:
            make(-down, right)
            make(-right, down)
            continue
        make(-down, -left)
        make(left, down)
        continue
    if right:
        make(up, right)
        make(-right, -up)
        continue
    make(up, -left)
    make(left, -up)
for t in range(len(tower)):
    i, j = tower[t]
    t = toweridx[(i, j)]
    left = False
    for k in range(j - 1, -1, -1):
        if company[i][k] == 'T':
            left = True
            break
        elif company[i][k] == '#':
            break
    if left:
        make(-t - 1, t + 1)
    else:
        right = False
        for k in range(j + 1, S):
            if company[i][k] == 'T':
                right = True
                break
            elif company[i][k] == '#':
                break
        if right:
            make(t + 1, -t - 1)
    up = False
    for k in range(i - 1, -1, -1):
        if company[k][j] == 'T':
            up = True
            break
        elif company[k][j] == '#':
            break
    if up:
        make(-t, t)
    else:
        down = False
        for k in range(i + 1, R):
            if company[k][j] == 'T':
                down = True
                break
            elif company[k][j] == '#':
                break
        if down:
            make(t, -t)
stack = []
visited = [False] * (2 * length + 1)
for i in range(-length, 0):
    if not visited[i]:
        dfs1(i)
for i in range(1, length + 1):
    if not visited[i]:
        dfs1(i)
idx = 0
visited = [-1] * (2 * length + 1)
while stack:
    cur = stack.pop()
    if visited[cur] == -1:
        dfs2(cur)
        idx += 1
ans = [0] * (length + 1)
for i in range(1, length + 1):
    if visited[i] > visited[-i]:
        ans[i] = 1
for i in range(len(tower)):
    cur = toweridx[tower[i]]
    tmp = '0'
    if not ans[cur + 1]:
        if ans[cur]:
            tmp = '1'
        else:
            tmp = '4'
    elif ans[cur]:
        tmp = '2'
    else:
        tmp = '3'
    company[tower[i][0]][tower[i][1]] = tmp
for i in range(R):
    print(''.join(company[i]))
