import sys

N = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
divider = [(i if i % 2 else 2) for i in range(5000001)]
for i in range(3, 5000001):
    if divider[i] == i:
        for j in range(i * i, 5000001, i * 2):
            if divider[j] == j:
                divider[j] = i
for n in k:
    while divider[n] != 1:
        print(divider[n], end=' ')
        n //= divider[n]
    print()
