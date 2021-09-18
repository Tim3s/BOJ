import sys
import math


def palindrome(n):
    while n:
        if n[0] != n[-1]:
            return False
        n = n[1:-1]
    return True


def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            return False
    return True


N = int(sys.stdin.readline())
if N == 1:
    print(2)
    sys.exit(0)
while True:
    if palindrome(str(N)) and prime(N):
        print(N)
        sys.exit(0)
    N += 1
