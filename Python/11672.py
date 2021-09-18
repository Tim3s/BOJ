import sys


def mergesort(cur):
    if len(cur) == 1:
        return cur
    half = len(cur) // 2
    left = mergesort(cur[:half])
    right = mergesort(cur[half:])
    global ans
    l = r = 0
    res = []
    while l != len(left) and r != len(right):
        if left[l] < right[r]:
            res.append(left[l])
            ans += r
            l += 1
        else:
            res.append(right[r])
            r += 1
    ans += r * (len(left) - l)
    return res + left[l:] + right[r:]


n = int(sys.stdin.readline())
camel = [[] for _ in range(n)]
for _ in range(3):
    tmp = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    for i in range(n):
        camel[tmp[i]].append(i)
camel.sort()
segment = [sys.maxsize] * (n * 4)
ans = 0
mergesort([camel[i][1] for i in range(n)])
mergesort([camel[i][2] for i in range(n)])
camel.sort(key=lambda x: x[1])
mergesort([camel[i][2] for i in range(n)])
print((n * (n - 1) - ans) // 2)
