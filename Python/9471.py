import sys

P = int(sys.stdin.readline())
for i in range(P):
    N, M = [int(i) for i in sys.stdin.readline().split()]
    a = 1
    b = 1
    i = 2
    while a != 1 or b != 0:
        a = (a + b) % M
        b = (a + b) % M
        i += 2
    if M == 2:
        i = 3
    print(N, i)
