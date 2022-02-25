import sys

N = int(sys.stdin.readline())
fossil = [sys.stdin.readline().rstrip() for _ in range(N)]
checked = [[False] * N for _ in range(N)]
loc = []
for i in range(N):
    for j in range(N):
        if not checked[i][j]:
            checked[i][j] = True
            if fossil[i][j] == '#':
                ni = i + 4
                while ni < N and fossil[ni][j] == '#':
                    ni += 1
                if fossil[(i + ni - 1) // 2][j + (ni - i - 1) // 2] == '#':
                    ni -= 1
                else:
                    ni += 1
                nj = j + ni - i
                direction = 'UL'
                if fossil[i][nj-1] == '.':
                    direction = 'UR'
                elif fossil[i+1][j] == '.':
                    direction = 'LU'
                elif fossil[i+1][nj] == '.':
                    direction = 'RU'
                elif fossil[ni-1][j] == '.':
                    direction = 'LD'
                elif fossil[ni-1][nj] == '.':
                    direction = 'RD'
                elif fossil[ni][j+1] == '.':
                    direction = 'DL'
                elif fossil[ni][nj-1] == '.':
                    direction = 'DR'
                loc.append([(i + ni) // 2 + 1, (j + nj) // 2 + 1, (ni - i + 1), direction])
                for tmpi in range(i, ni + 1):
                    for tmpj in range(j, nj + 1):
                        checked[tmpi][tmpj] = True
loc.sort()
print(len(loc))
for tmp in loc:
    print(*tmp)
