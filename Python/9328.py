import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    world = [['.'] * (w + 2)] + [['.'] + list(sys.stdin.readline().rstrip()) + ['.'] for _ in range(h)] + [['.'] * (w + 2)]
    key = set(list(sys.stdin.readline().rstrip()))
    q = deque()
    h += 2
    w += 2
    visited = [[False] * w for _ in range(h)]
    visited[0][0] = True
    q.append((0, 0))
    locked = dict()
    ans = 0
    while q:
        x, y = q.popleft()
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                visited[nx][ny] = True
                if world[nx][ny] == '*':
                    continue
                if world[nx][ny].isupper():
                    if world[nx][ny].lower() in key:
                        q.append((nx, ny))
                    else:
                        locked[(nx, ny)] = world[nx][ny].lower()
                    continue
                if world[nx][ny].islower():
                    todelete = []
                    key.add(world[nx][ny])
                    for loc in locked:
                        if locked[loc] == world[nx][ny]:
                            todelete.append(loc)
                            q.append(loc)
                    for loc in todelete:
                        del locked[loc]
                elif world[nx][ny] == '$':
                    ans += 1
                q.append((nx, ny))
    print(ans)
