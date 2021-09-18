import sys


def cantor(start, n):
    if n == 1:
        return
    n //= 3
    for i in range(start + n, start + 2 * n):
        ans[i] = ' '
    cantor(start, n)
    cantor(start + 2 * n, n)


num = []
while True:
    try:
        num.append(int(sys.stdin.readline()))
    except:
        break
for N in num:
    if N == 0:
        print('-')
    else:
        ans = ['-'] * (3 ** N)
        cantor(0, 3 ** N)
        print(''.join(ans))
