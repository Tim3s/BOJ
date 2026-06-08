def swap(world, i, j, ii, jj):
    tmp = world[i][j]
    world[i][j] = world[ii][jj]
    world[ii][jj] = tmp
    return world

def search(world, i, j, ii, jj):
    world = swap(world, i, j, ii, jj)
    CPZY = [[[0 for _ in range(2)] for _ in range(N)] for _ in range(N)]
    for m in range(N):
        for n in range(N):
            if m + 1 != N and world[m][n] == world[m+1][n]:
                CPZY[m+1][n][0] = CPZY[m][n][0] + 1
            if n + 1 != N and world[m][n] == world[m][n+1]:
                CPZY[m][n+1][1] = CPZY[m][n][1] + 1
    world = swap(world, i, j, ii, jj)
    return max([CPZY[i][j][k] for i in range(N) for j in range(N) for k in range(2)]) + 1

N = int(input())
world = [list(input()) for _ in range(N)]
res = 1
for i in range(N):
    for j in range(N):
        if i+1 < N:
            res = max(search(world, i, j, i+1, j), res)
        if j+1 < N:
            res = max(search(world, i, j, i, j + 1), res)
print(res)
