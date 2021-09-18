import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    tree = [Node(i) for i in range(N + 1)]
    for _ in range(N - 1):
        A, B = map(int, sys.stdin.readline().split())
        tree[B].parent = A
    A, B = map(int, sys.stdin.readline().split())
    AP = []
    while A:
        AP.append(A)
        A = tree[A].parent
    BP = []
    while B:
        BP.append(B)
        B = tree[B].parent
    if len(AP) == len(BP) == 1:
        print(A)
    else:
        a = len(AP) - 1
        b = len(BP) - 1
        while AP[a - 1] == BP[b - 1]:
            a -= 1
            b -= 1
        print(AP[a])
