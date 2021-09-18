import sys

N = int(sys.stdin.readline())
curmax = curmin = list(map(int, sys.stdin.readline().split()))
for _ in range(N - 1):
    tmp = list(map(int, sys.stdin.readline().split()))
    curmax = [max(curmax[0], curmax[1]) + tmp[0], max(curmax) + tmp[1], max(curmax[1], curmax[2]) + tmp[2]]
    curmin = [min(curmin[0], curmin[1]) + tmp[0], min(curmin) + tmp[1], min(curmin[1], curmin[2]) + tmp[2]]
print(max(curmax), min(curmin))
