import sys

N = int(sys.stdin.readline())
loc = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
tmpsum = 0
for i in range(N):
    tmpsum += loc[i][0] * loc[i - 1][1] - loc[i][1] * loc[i - 1][0]
print(format(abs(tmpsum) / 2, '.1f'))
