import sys
from collections import deque


def left(r, b):
    if r[1] < b[1]:
        for k in range(r[1], 0, -1):
            if board[r[0]][k - 1] == '#':
                r = [r[0], k]
                break
            elif board[r[0]][k - 1] == 'O':
                if r[0] == b[0]:
                    for idx in range(r[1] + 1, b[1] + 1):
                        if idx == b[1]:
                            return False
                        if board[r[0]][idx] == '#':
                            break
                return True
        for k in range(b[1], 0, -1):
            if board[b[0]][k - 1] == '#' or [b[0], k - 1] == r:
                b = [b[0], k]
                break
            elif board[b[0]][k - 1] == 'O':
                return False
    else:
        for k in range(b[1], 0, -1):
            if board[b[0]][k - 1] == '#':
                b = [b[0], k]
                break
            elif board[b[0]][k - 1] == 'O':
                return False
        for k in range(r[1], 0, -1):
            if board[r[0]][k - 1] == '#' or [r[0], k - 1] == b:
                r = [r[0], k]
                break
            elif board[r[0]][k - 1] == 'O':
                return True
    return r, b


def right(r, b):
    if r[1] > b[1]:
        for k in range(r[1], M - 1):
            if board[r[0]][k + 1] == '#':
                r = [r[0], k]
                break
            elif board[r[0]][k + 1] == 'O':
                if r[0] == b[0]:
                    for idx in range(r[1] - 1, b[1] - 1, -1):
                        if idx == b[1]:
                            return False
                        if board[r[0]][idx] == '#':
                            break
                return True
        for k in range(b[1], M - 1):
            if board[b[0]][k + 1] == '#' or [b[0], k + 1] == r:
                b = [b[0], k]
                break
            elif board[b[0]][k + 1] == 'O':
                return False
    else:
        for k in range(b[1], M - 1):
            if board[b[0]][k + 1] == '#':
                b = [b[0], k]
                break
            elif board[b[0]][k + 1] == 'O':
                return False
        for k in range(r[1], M - 1):
            if board[r[0]][k + 1] == '#' or [r[0], k + 1] == b:
                r = [r[0], k]
                break
            elif board[r[0]][k + 1] == 'O':
                return True
    return r, b


def up(r, b):
    if r[0] < b[0]:
        for k in range(r[0], 0, -1):
            if board[k - 1][r[1]] == '#':
                r = [k, r[1]]
                break
            elif board[k - 1][r[1]] == 'O':
                if r[1] == b[1]:
                    for idx in range(r[0] + 1, b[0] + 1):
                        if idx == b[0]:
                            return False
                        if board[idx][r[1]] == '#':
                            break
                return True
        for k in range(b[0], 0, -1):
            if board[k - 1][b[1]] == '#' or [k - 1, b[1]] == r:
                b = [k, b[1]]
                break
            elif board[k - 1][b[1]] == 'O':
                return False
    else:
        for k in range(b[0], 0, -1):
            if board[k - 1][b[1]] == '#':
                b = [k, b[1]]
                break
            elif board[k - 1][b[1]] == 'O':
                return False
        for k in range(r[0], 0, -1):
            if board[k - 1][r[1]] == '#' or [k - 1, r[1]] == b:
                r = [k, r[1]]
                break
            elif board[k - 1][r[1]] == 'O':
                return True
    return r, b


def down(r, b):
    if r[0] > b[0]:
        for k in range(r[0], N - 1):
            if board[k + 1][r[1]] == '#':
                r = [k, r[1]]
                break
            elif board[k + 1][r[1]] == 'O':
                if r[1] == b[1]:
                    for idx in range(r[0] - 1, b[0] - 1, -1):
                        if idx == b[0]:
                            return False
                        if board[idx][r[1]] == '#':
                            break
                return True
        for k in range(b[0], N - 1):
            if board[k + 1][b[1]] == '#' or [k + 1, b[1]] == r:
                b = [k, b[1]]
                break
            elif board[k + 1][b[1]] == 'O':
                return False
    else:
        for k in range(b[0], N - 1):
            if board[k + 1][b[1]] == '#':
                b = [k, b[1]]
                break
            elif board[k + 1][b[1]] == 'O':
                return False
        for k in range(r[0], N - 1):
            if board[k + 1][r[1]] == '#' or [k + 1, r[1]] == b:
                r = [k, r[1]]
                break
            elif board[k + 1][r[1]] == 'O':
                return True
    return r, b


N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
q = deque()
R = [0, 0]
B = [0, 0]
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == 'R':
            R = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'B':
            B = [i, j]
            board[i][j] = '.'
q.append((R, B, 0))
ans = -1
while q:
    R, B, time = q.popleft()
    if time == 10:
        print(-1)
        sys.exit(0)
    time += 1
    for nboard in [left(R, B), right(R, B), up(R, B), down(R, B)]:
        if nboard == True:
            print(time)
            sys.exit(0)
        elif nboard:
            q.append((nboard[0], nboard[1], time))
print(-1)
