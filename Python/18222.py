import sys


def txt(cur):
    if cur == 1:
        return 0
    nextone = 1
    while nextone * 2 < cur:
        nextone *= 2
    return 1 - txt(cur - nextone)


k = int(sys.stdin.readline())
print(txt(k))
