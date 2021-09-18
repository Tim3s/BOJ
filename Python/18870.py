import sys
from collections import Counter

ln = int(sys.stdin.readline())
num = [int(i) for i in sys.stdin.readline().split()]
cnt = sorted(Counter(num).items())
length = len(cnt)
cnt.sort()
cnt = {cnt[i][0] : i for i in range(length)}
for i in num:
    print(cnt[i], end=' ')
