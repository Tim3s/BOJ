import sys

loop = int(sys.stdin.readline())
q = []
cnt = 0
for i in range(loop):
    cur = sys.stdin.readline().split()
    if cur[0] == "push":
        q.append(cur[1])
    elif cur[0] == "size":
        print(len(q) - cnt)
    elif cur[0] == "empty":
        print(int(len(q) == cnt))
    elif len(q) == cnt:
        print(-1)
    elif cur[0] == "front":
        print(q[cnt])
    elif cur[0] == "back":
        print(q[-1])
    else:
        print(q[cnt])
        cnt += 1
