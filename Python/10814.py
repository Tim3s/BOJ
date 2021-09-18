import sys

ln = int(sys.stdin.readline())
txt = [input().split() for j in range(ln)]
txt.sort(key=lambda x: (int(x[0])))
for i in txt:
    print(i[0], i[1])
