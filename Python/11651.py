import sys

ln = int(sys.stdin.readline())
num = [[int(i) for i in sys.stdin.readline().split()] for j in range(ln)]
num.sort(key=lambda x: (x[1], x[0]))
for i in num:
    print(i[0], i[1])
