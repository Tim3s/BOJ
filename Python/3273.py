import sys

n = int(sys.stdin.readline())
num = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())
i = 0
j = n - 1
cnt = 0
while i != j:
    if num[i] + num[j] == x:
        cnt += 1
        if num[i] == num[i + 1]:
            i += 1
            continue
        j -= 1
        continue
    if num[i] + num[j] > x:
        j -= 1
        continue
    i += 1
print(cnt)
