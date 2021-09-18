import math
import sys

ans = [0, 3]
for i in range(2, 1001):
    cnt = 0
    for j in range(i + 1):
        if math.gcd(i, j) == 1:
            cnt += 1
    ans.append(ans[-1] + 2 * cnt)
C = int(sys.stdin.readline())
for _ in range(C):
    print(ans[int(sys.stdin.readline())])
