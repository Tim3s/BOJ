import sys

M = int(sys.stdin.readline())
S = 0

for i in range(M):
    mystr = sys.stdin.readline().split()
    if mystr[0] == 'all':
        S = (1 << 20) - 1
        continue
    if mystr[0] == 'empty':
        S = 0
        continue
    command, num = mystr[0], int(mystr[1])
    num -= 1
    if command == "add":
        S |= 1 << num
    elif command == "check":
        print(1 if S & 1 << num else 0)
    elif command == "remove":
        S &= ~(1 << num)
    else:
        S ^= 1 << num
