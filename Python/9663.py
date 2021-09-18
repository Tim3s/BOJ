import sys


def correctness(n):
    for i in range(n):
        if loc[n] == loc[i] or n - i == abs(loc[n] - loc[i]):
            return False
    return True


def find(n):
    global ncase
    if n == N:
        ncase += 1
    else:
        for i in range(N):
            loc[n] = i
            if correctness(n):
                find(n + 1)


N = int(sys.stdin.readline())
loc = [0] * N
ncase = 0
find(0)
print(ncase)
