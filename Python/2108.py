import sys
from collections import Counter

ln = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for i in range(ln)]
print(round(sum(num) / ln))
num.sort()
print(num[ln // 2])
freq = Counter(num).most_common(2)
if len(freq) > 1:
    if freq[0][1] == freq[1][1]:
        print(freq[1][0])
    else:
        print(freq[0][0])
else:
    print(freq[0][0])

print(num[-1] - num[0])
