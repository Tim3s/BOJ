import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))
    res = '0'
    for i in range(1, n):
        if (x[i-1] | x[i]) != x[i]:
            res += ' ' + str((x[i-1] | x[i]) - x[i])
            x[i] = x[i] | x[i-1]
        else:
            res += ' 0'
    print(res)
