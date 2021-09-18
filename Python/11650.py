import sys

ln = int(sys.stdin.readline())
num = [[int(i) for i in input().split()] for j in range(ln)]
num.sort()
for i in num:
    print(i[0], i[1])
