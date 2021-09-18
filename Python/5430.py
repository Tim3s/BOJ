import sys
from collections import deque

loop = int(sys.stdin.readline())
for i in range(loop):
    mystr = sys.stdin.readline().strip()
    length = int(sys.stdin.readline())
    num = deque(sys.stdin.readline().strip("\n[]").split(','))
    if mystr.count('D') > length:
        print("error")
    else:
        right = True
        for char in mystr:
            if char == 'R':
                right = not right
            else:
                if right:
                    num.popleft()
                else:
                    num.pop()
        if not right:
            num.reverse()
        print('[' + ','.join(list(num)) + ']')
