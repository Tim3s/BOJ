import sys

T = int(sys.stdin.readline())
res = [1, 2, 4]
for i in range(3, 11):
    res.append(res[-1] + res[-2] + res[-3])
for i in range(T):
    print(res[int(sys.stdin.readline()) - 1])
