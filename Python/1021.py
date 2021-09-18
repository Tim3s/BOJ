import sys

NM = [int(i) for i in sys.stdin.readline().split()]
q = [i for i in range(1, NM[0] + 1)]
num = [int(i) for i in sys.stdin.readline().split()]
index = 0
res = 0
for i in range(NM[1]):
    newindex = q.index(num[i])
    tmp = abs(newindex - index)
    res += min(tmp, len(q) - tmp)
    del q[newindex]
    if len(q) != 0:
        index = newindex % len(q)
print(res)
