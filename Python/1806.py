import sys

N, S = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
i = 0
j = 0
tmpsum = 0
ans = 100000001
while tmpsum >= S or j != N:
    if tmpsum >= S:
        ans = min(ans, j - i)
        tmpsum -= num[i]
        i += 1
        continue
    tmpsum += num[j]
    j += 1
print(0 if ans == 100000001 else ans)
