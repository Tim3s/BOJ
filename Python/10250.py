import math

ln = int(input())
for nothing in range(ln):
    tmp = input().split()
    H = int(tmp[0])
    N = int(tmp[2])
    Y = (N - 1) % H + 1
    X = math.ceil(N / H)
    if X < 10:
        print(Y, 0, X, sep='')
    else:
        print(Y, X, sep='')
