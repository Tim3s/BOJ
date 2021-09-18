import sys


def gcd(a, b):
    if b == 0:
        return a, (1, 0)
    res = gcd(b, a % b)
    return res[0], (res[1][1], res[1][0] - (a // b) * res[1][1])


t = int(sys.stdin.readline())
for _ in range(t):
    K, C = map(int, sys.stdin.readline().split())
    # if K == 1:
    #     print(2 if C == 1 else 1)
    #     continue
    ans = gcd(C, K)
    if ans[0] != 1:
        print('IMPOSSIBLE')
    else:
        tmp = ans[1][0] % K
        while tmp * C <= K:
            tmp += K
        if tmp > 10 ** 9:
            print('IMPOSSIBLE')
        else:
            print(tmp)
