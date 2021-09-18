import sys

N = int(sys.stdin.readline())
num = [0] + list(map(int, sys.stdin.readline().split()))
ans = []
for i in range(1, N + 1):
    if num[i] == 0:
        ans.append(i)
    else:
        ans.insert(len(ans) - num[i], i)
print(*ans)
