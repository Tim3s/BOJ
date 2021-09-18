import sys
from itertools import combinations

ln = int(sys.stdin.readline())
num = [[int(i) for i in sys.stdin.readline().split()] for j in range(ln)]
com = list(combinations([str(i) for i in range(ln)], ln // 2))
com = [[int(i) for i in com[j]] for j in range(len(com) // 2)]
mymin = 1000000

for item in com:
    tmp1 = 0
    tmp2 = 0
    tmplist = [i for i in range(ln) if i not in item]
    for i in range(ln // 2):
        for j in range(ln // 2):
            tmp1 += num[item[i]][item[j]]
            tmp2 += num[tmplist[i]][tmplist[j]]
    mymin = min(mymin, abs(tmp1 - tmp2))
print(mymin)
