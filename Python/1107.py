from collections import deque
import sys


def check(a):
    for char in a:
        if char in broken:
            return False
    return True


d = deque()
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken = sys.stdin.readline().split()
res = [abs(N - 100)]
index = N
while index >= 0:
    if check(str(index)):
        break
    index -= 1
if index != -1:
    res.append(max(len(str(index)), 1) + N - index)
index = N
while index <= 999999:
    if check(str(index)):
        break
    index += 1
if index != 1000000:
    res.append(len(str(index)) + index - N)
print(min(res))
