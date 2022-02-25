import sys
N = int(sys.stdin.readline())
if N <= 2:
    print(0)
    sys.exit()
a = list(map(int, sys.stdin.readline().split()))
up = down = -1
upvalid = True
downvalid = True
for i in range(N):
    if a[i] == a[i-1]:
        continue
    if a[i] > a[i-1]:
        if down == -1:
            down = i
        else:
            downvalid = False
        continue
    if up == -1:
        up = i
    else:
        upvalid = False
if up == -1 or down == -1:
    print(0)
elif upvalid and downvalid:
    print(min(up, down))
elif upvalid:
    print(up)
elif downvalid:
    print(down)
else:
    print(-1)
