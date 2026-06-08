import sys

R, C = map(int, sys.stdin.readline().split())
world = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if world[i][j] == '.':
            world[i][j] = 'D'
        elif world[i][j] == 'W':
            if i and world[i-1][j] == 'S' or j and world[i][j-1] == 'S' or i < R-1 and world[i+1][j] == 'S' or j < C-1 and world[i][j+1] == 'S':
                print(0)
                sys.exit(0)
print(1)
for line in world:
    print(''.join(line))
