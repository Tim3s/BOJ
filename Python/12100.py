import sys
import copy


def left():
    global game
    for i in range(N):
        idx = 0
        check = 0
        for j in range(N):
            if game[i][j]:
                if check:
                    if check == game[i][j]:
                        game[i][idx] = check * 2
                        check = 0
                    else:
                        game[i][idx] = check
                        check = game[i][j]
                    idx += 1
                else:
                    check = game[i][j]
                game[i][j] = 0
        if check:
            game[i][idx] = check


def right():
    global game
    for i in range(N):
        idx = N - 1
        check = 0
        for j in range(N - 1, -1, -1):
            if game[i][j]:
                if check:
                    if check == game[i][j]:
                        game[i][idx] = check * 2
                        check = 0
                    else:
                        game[i][idx] = check
                        check = game[i][j]
                    idx -= 1
                else:
                    check = game[i][j]
                game[i][j] = 0
        if check:
            game[i][idx] = check


def up():
    global game
    for j in range(N):
        idx = 0
        check = 0
        for i in range(N):
            if game[i][j]:
                if check:
                    if check == game[i][j]:
                        game[idx][j] = check * 2
                        check = 0
                    else:
                        game[idx][j] = check
                        check = game[i][j]
                    idx += 1
                else:
                    check = game[i][j]
                game[i][j] = 0
        if check:
            game[idx][j] = check


def down():
    global game
    for j in range(N):
        idx = N - 1
        check = 0
        for i in range(N - 1, -1, -1):
            if game[i][j]:
                if check:
                    if check == game[i][j]:
                        game[idx][j] = check * 2
                        check = 0
                    else:
                        game[idx][j] = check
                        check = game[i][j]
                    idx -= 1
                else:
                    check = game[i][j]
                game[i][j] = 0
        if check:
            game[idx][j] = check


def dfs(n):
    global game
    if n == 5:
        return max([max(game[i]) for i in range(N)])
    n += 1
    cur = copy.deepcopy(game)
    res = 0
    left()
    res = max(res, dfs(n))
    game = copy.deepcopy(cur)
    right()
    res = max(res, dfs(n))
    game = copy.deepcopy(cur)
    up()
    res = max(res, dfs(n))
    game = copy.deepcopy(cur)
    down()
    return max(res, dfs(n))


N = int(sys.stdin.readline())
game = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(dfs(0))
