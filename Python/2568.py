import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
num = [-1] * 500001
Aset = set()
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    Aset.add(A)
    num[A] = B
length = []
lcur = []
back = [-1] * 500001
for i in range(len(num)):
    n = num[i]
    if n != -1:
        tmp = bisect_left(length, n)
        if tmp != 0:
            back[i] = lcur[tmp - 1]
        if tmp == len(length):
            length.append(n)
            lcur.append(i)
        else:
            length[tmp] = n
            lcur[tmp] = i
print(N - len(length))
cur = lcur[-1]
ans = []
while cur != -1:
    Aset.remove(cur)
    cur = back[cur]
print('\n'.join(list(map(str, sorted(list(Aset))))))
