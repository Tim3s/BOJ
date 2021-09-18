import sys
import bisect


def dp(left, right, pos, candies, cur):
    global ans
    if memo[left][right][pos][0] >= cur and candies <= memo[left][right][pos][1]:
        return
    if candies <= 0 or (left == 0 and right == n):
        ans = max(ans, cur)
        return
    memo[left][right][pos] = [cur, candies]
    loc = right if pos else left
    if left:
        dp(left - 1, right, 0, candies - (candy[loc] - candy[left - 1]), cur + max(candies + candy[left - 1] - candy[loc], 0))
    if right < n:
        dp(left, right + 1, 1, candies - candy[right + 1] + candy[loc], cur + max(0, candies - candy[right + 1] + candy[loc]))


n, m = map(int, sys.stdin.readline().split())
candy = [0]
for _ in range(n):
    candy.append(int(sys.stdin.readline()))
candy.sort()
start = bisect.bisect_left(candy, 0)
memo = [[[[-1, -1] for _ in range(2)] for _ in range(n + 1)] for _ in range(n + 1)]
ans = 0
dp(start, start, 0, m, 0)
print(ans)
