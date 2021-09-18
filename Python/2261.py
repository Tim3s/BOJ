import sys
import math


def calc(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2


def cond(a, b):
    return True if a[1] < b[1] else a[0] < b[0]


def d(left, right):
    mid = (left + right) // 2
    if left + 1 >= right:
        return 800000000
    mymin = min(d(left, mid), d(mid, right))
    mylist = []
    squared = math.sqrt(mymin)
    for i in range(mid, left - 1, -1):
        if abs(num[mid][0] - num[i][0]) < squared:
            mylist.append(num[i])
    for i in range(mid + 1, right):
        if abs(num[mid][0] - num[i][0]) < squared:
            mylist.append(num[i])
    mylist = sorted(mylist, key=lambda x: (x[1], x[0]))
    for i in range(len(mylist)):
        for j in range(i + 1, len(mylist)):
            if mylist[j][1] - mylist[i][1] > squared:
                break
            mymin = min(mymin, calc(mylist[i], mylist[j]))
            squared = math.sqrt(mymin)
    return mymin


n = int(sys.stdin.readline())
num = sorted([[int(i) for i in sys.stdin.readline().split()] for j in range(n)])
print(d(0, n))
