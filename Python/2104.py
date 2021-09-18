import sys


def dfs(left, right):
    if left == right:
        return num[left] ** 2
    mid = (left + right) // 2
    res = max(dfs(left, mid), dfs(mid + 1, right))
    tmpleft = mid
    tmpright = mid + 1
    tmpsum = num[tmpleft] + num[tmpright]
    tmpmin = min(num[tmpleft], num[tmpright])
    res = max(res, tmpsum * tmpmin)
    while tmpleft > left or tmpright < right:
        if tmpleft > left and (tmpright == right or num[tmpleft - 1] > num[tmpright + 1]):
            tmpleft -= 1
            tmpsum += num[tmpleft]
            tmpmin = min(tmpmin, num[tmpleft])
        else:
            tmpright += 1
            tmpsum += num[tmpright]
            tmpmin = min(tmpmin, num[tmpright])
        res = max(res, tmpsum * tmpmin)
    return res


N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
print(dfs(0, N - 1))
