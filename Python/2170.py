import sys

N = int(sys.stdin.readline())
line = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    line.append((a, b))
line.sort()
ans = 0
start = -2000000000
end = -2000000000
for a, b in line:
    if end < a:
        ans += end - start
        start = a
        end = b
    elif end < b:
        end = b
ans += end - start
print(ans)
