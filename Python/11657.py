import sys
import copy

class Node:
    def __init__(self, v=None, w=None):
        self.v = v
        self.w = w
        self.next = None


class LinkedList:
    def __init__(self):
        self.__header = None

    def append(self, x, l):
        tmpNode = Node(x, l)
        tmpNode.next = self.__header
        self.__header = tmpNode

    def header(self):
        return self.__header


N, M = map(int, sys.stdin.readline().split())
bus = []
for _ in range(M):
    bus.append(list(map(int, sys.stdin.readline().split())))
ans = [10000000] * (N + 1)
ans[1] = 0
for _ in range(N - 1):
    for A, B, C in bus:
        if ans[B] != 10000000:
            ans[B] = min(ans[B], ans[A] + C)
        elif ans[A] != 10000000:
            ans[B] = ans[A] + C
check = copy.deepcopy(ans)
for A, B, C in bus:
    if check[B] != 10000000:
        check[B] = min(check[B], check[A] + C)
    elif check[A] != 10000000:
        check[B] = check[A] + C
if ans != check:
    print(-1)
    sys.exit(0)
for i in range(2, N + 1):
    print(-1 if ans[i] == 10000000 else ans[i])
