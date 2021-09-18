import sys

tmpsum = 2000000001
N = int(sys.stdin.readline())
num = sorted(list(map(int, sys.stdin.readline().split())))
i = 0
j = N - 1
ans = 0
while i != j:
    tmp = num[i] + num[j]
    if abs(tmp) < tmpsum:
        ans = [num[i], num[j]]
        tmpsum = abs(tmp)
    if tmp >= 0:
        j -= 1
        continue
    i += 1
print(ans[0], ans[1])
