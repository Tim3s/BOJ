import sys
from itertools import product

NM = [int(i) for i in sys.stdin.readline().split()]
numlist = [str(i) for i in range(1, NM[0] + 1)]
num = product(numlist, repeat=NM[1])
for item in num:
    print(' '.join(item))
