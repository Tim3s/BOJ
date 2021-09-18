import sys

N = int(sys.stdin.readline())
num = sorted(list(map(int, sys.stdin.readline().split())))
tmpsum = 3000000001
ans = 0
for i in range(N - 2):
    left = i + 1
    right = N - 1
    while left != right:
        tmp = num[i] + num[left] + num[right]
        if abs(tmp) < tmpsum:
            ans = [num[i], num[left], num[right]]
            tmpsum = abs(tmp)
        if tmp < 0:
            left += 1
        else:
            right -= 1
print(*ans)
