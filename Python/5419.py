import sys
import bisect


def update(x):
    while x <= length:
        tree[x] += 1
        x += x & -x


def getsum(x):
    res = 0
    while x:
        res += tree[x]
        x -= x & -x
    return res


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    isle = []
    num = set()
    for _ in range(n):
        isle.append(list(map(int, sys.stdin.readline().split())))
        isle[-1][1] *= -1
        num.add(isle[-1][1])
    isle.sort()
    nums = [-10 ** 9 - 1] + sorted(list(num))
    length = len(nums)
    tree = [0] * (length + 1)
    ans = 0
    for i in range(n):
        tmp = bisect.bisect_left(nums, isle[i][1])
        ans += getsum(tmp)
        update(tmp)
    print(ans)
