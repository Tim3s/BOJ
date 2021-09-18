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
num = list(map(int, sys.stdin.readline().split()))
ans = 0
mergesort(num)
print(ans)
