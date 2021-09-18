import sys


def dfs(x, y, visited):
    res = 0
    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if 0 <= nx < R and 0 <= ny < C and not visited & 1 << board[nx][ny]:
            res = max(res, dfs(nx, ny, visited | 1 << board[nx][ny]))
    res += 1
    return res


R, C = map(int, sys.stdin.readline().split())
board = [list(map(lambda x: ord(x) - 65, list(sys.stdin.readline().rstrip()))) for _ in range(R)]
print(dfs(0, 0, 1 << board[0][0]))
