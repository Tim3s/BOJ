import sys

ln = int(sys.stdin.readline())
txt = list(set([input() for j in range(ln)]))
txt.sort(key=lambda x: (len(x), x))
for i in txt:
    print(i)
