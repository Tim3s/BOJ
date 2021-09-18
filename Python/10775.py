import sys


def docking(last):
    global done
    cur = last
    while back[cur]:
        cur = back[cur]
    if cur == 1:
        if done:
            return False
        done = True
    back[last] = cur
    back[cur] = cur - 1
    return True


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
back = [0] * (G + 1)
ans = 0
done = False
for _ in range(P):
    g = int(sys.stdin.readline())
    if docking(g):
        ans += 1
    else:
        break
print(ans)
